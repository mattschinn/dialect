// test_find_files.js (or whatever you want to name it)

const fs = require('fs');
const path = require('path');

function findFilesInFolder(folderPath, substring) {
    try {
        const files = fs.readdirSync(folderPath);
        const matchingFiles = [];

        console.log("Files in folder:", files); // Helpful for debugging

        for (const file of files) {
            const filePath = path.join(folderPath, file);
            const stats = fs.statSync(filePath);

            if (stats.isFile()) {
                if (file.includes(substring)) {
                    matchingFiles.push(filePath);
                }
            }
        }

        return matchingFiles;
    } catch (err) {
        console.error("Error reading folder:", err);
        return [];
    }
}

// Test cases:  This is where you'll exercise your function!
const testFolder = './entries/cup_of_joe/'; // Create this folder and some files inside!
const testSubstring = 'png';

// 1. Folder exists, files match:
const foundFiles1 = findFilesInFolder(testFolder, testSubstring);
console.log("Test 1 (files found):", foundFiles1);
