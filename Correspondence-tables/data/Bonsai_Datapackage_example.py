import datapackage


# Get data for a specific file.
package = datapackage.Package()
package.infer('ISICv4_to_NACEv2/ISICv4_to_NACEv2.csv') #  Select a file and automatically determine structure
#package.infer('**/*.csv'). # Use this to apply to all files in the folder, if there are more than one
print(package.descriptor)

# Modify the descriptor
print(package.descriptor['resources'][0]['schema']['fields']) # The 'ISIC4code' shuold be a string...same with the NACE2code. We must change them.
package.descriptor['resources'][0]['schema']['fields'][0]['type'] = 'string' 
package.descriptor['resources'][0]['schema']['fields'][2]['type'] = 'string' 
print(package.descriptor['resources'][0]['schema']['fields'])

# Set other properties
### (see here for details: https://frictionlessdata.io/specs/data-package/)

# Mandatory properties:
## Title
package.descriptor['title'] = 'ISICv4_to_NACEv2' # different from name because human readable.

## ID
package.descriptor['id'] = 'alsækjdqwilullkjashdflkj' # I guess it will be some URI

## Licenses
package.descriptor['licenses'] = [{ "name": "MIT", "path": "https://opensource.org/licenses/MIT", "title": "The MIT License"}]

## Profile 
### (This will be set up automatticlaly form "infer")

# Optional properties
## Sources
package.descriptor['sources'] = {"title": "United Nations ", "path": "http://data.un.org/"}

## Description
package.descriptor['description'] = 'Classification of Economic Activities in the European Community'

## Contributors
package.descriptor['contributors'] =  [{"title": "Massimo Pizzol", "email": "massimo@plan.aau.dk", "path": "https://github.com/massimopizzol", "role": "author"}]

## Created
package.descriptor['created'] = "2019-03-25"



# Implement changes and save
print(package.descriptor)
package.commit()
package.save('ISICv4_to_NACEv2/datapackage.json') # This MUST be the name. Place in the top directory.


# Test that it works
dp = datapackage.Package('ISICv4_to_NACEv2/datapackage.json')
print(dp.descriptor)
