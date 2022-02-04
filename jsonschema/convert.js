const convert = require('json-schema-to-openapi-schema');
const fs = require('fs')
const filepath = "alienvault.json"

const schema = {
	 	'$schema': 'http://json-schema.org/draft-04/schema#',
		type: ['string', 'null'],
		format: 'date-time',
};

try {
  const data = fs.readFileSync(filepath, 'utf8')
  console.log(data)
	console.log("\n=================================")
	console.log("Succesfully loaded data!")
	console.log("=================================\n")

	const convertedSchema = convert(schema);
	const stringified = JSON.stringify(convertedSchema)

	console.log("Done translating")
	const new_filename = "new_"+filepath
	fs.writeFile(new_filename, stringified,  function (err) {
  	if (err) return console.log(err);
  	//console.log('Hello World > helloworld.txt');
		console.log("\n=================================")
		console.log("Wrote to file ", new_filename, "!!!!")
		console.log("=================================\n")
	})

} catch (err) {
  console.error("An error occured: ", err)
}


