function instAndStuds() {

var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

var stud = users.Students;
var inst = users.Instructors;

console.log("Students");
for (var name in stud) {
    console.log((parseInt(name)+1)+ " " +stud[name].first_name+ " "+ stud[name].last_name + " - "+(stud[name].first_name.length + stud[name].last_name.length));
}
console.log("Instructors");
   for (var name in inst) {
     console.log((parseInt(name)+1)+ " "+ inst[name].first_name+ " "+ inst[name].last_name + " - "+(inst[name].first_name.length + inst[name].last_name.length));
   }
}
instAndStuds();