#!/usr/bin/node
// 8-esrever.js

exports.esrever = function (list) {
    const reversedList = [];
    for (let i = list.length - 1; i >= 0; i--) {
        reversedList.push(list[i]);
    }
    return reversedList;
};
