import datapackage
package = datapackage.Package()
package.infer('final_tables/tables/*.csv')
print(package.descriptor)
print(package.valid)
print(package.errors)
package.save('final_tables/tables/datapackage.json')