# Hash-text-files
 This script generates hashes from every line of a text file.
 
 It produces md5, sha1, sha256, sha512 files as the output. I will be adding more hashes in the future.
 
  
 At the end of the hash a {\t => \t} is placed, to clearly define the start and end of the string. 
 Example of the output file in sha256:
 
 ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb	=>	a
 3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d	=> b
 2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6	=>	c
 
 .
 .
 
 

 
 Every hash function in this script is processed in a separate thread.
 
 # How to use
 You have to edit the parameters in the file to match what you want, I left it configured for the text.txt file already there, as an example.

 Remember to edit the encoding, since each file can be different. For example, the most common ones are "utf-8" and "ansi". Check before using.

 The text file in here serves as an example of how the formatting should be for the script to work.

 To run it just execute in the CMD or in the Terminal with Python3.6+.
