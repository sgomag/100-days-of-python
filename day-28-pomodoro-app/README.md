# Day 28 - Pomodoro Timer

A Pomodoro timer built with Tkinter.

The app cycles through 25-minute work sessions and 5-minute breaks, with a longer break of 20-minutes after every four work sessions. The background changes color to signal work or break mode, and a pop-up notification announces each new round. Completed work sessions are tracked with checkmarks, and every four sessions the user earns a tomato icon. The user can start, pause, resume, and reset the timer at any point.

This is my first GUI app. The main thing I learned was how `window.after` works, which is the motor of the timer.