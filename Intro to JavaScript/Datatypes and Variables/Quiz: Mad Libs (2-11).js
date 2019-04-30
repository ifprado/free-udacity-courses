/*
 * Programming Quiz: MadLibs (2-11)
 *
 * 1. Declare a madLib variable
 * 2. Use the adjective1, adjective2, and adjective3 variables to set the madLib variable to the message:
 *
 * 'The Intro to JavaScript course is amazing. James and Julia are so fun. I cannot wait to work through the rest of this entertaining content!'
 */

var adjective1 = 'amazing';
var adjective2 = 'fun';
var adjective3 = 'entertaining';

// your code goes here
var madLib = "The Intro to JavaScript course is __________. James and Julia are so __________. I cannot wait to work through the rest of this __________ content!";
madLib = madLib.replace("__________",adjective1).replace("__________",adjective2).replace("__________",adjective3);
console.log(madLib);
