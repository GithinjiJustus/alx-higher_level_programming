#!/usr/bin/node
// 7-occurrences.js

exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    for (const element of list) {
        if (element === searchElement) {
            count++;
        }
    }
    return count;
};
