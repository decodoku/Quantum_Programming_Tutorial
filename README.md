# Hello Quantum

Do you want to program quantum computers, but don't know where to start? Then you have found the right place! Here you will find a gamified tutorial to quantum programming, which will guide you in the creation of your first quantum programs.

This tutorial is currently in beta, and so content will be added over time. **We are seeking any and all feedback throughout this process to help us build the finished product.**

You can start off with **Story Mode**, which will introduce you to the basics of manipulating quantum information. Each level is presented as a simple puzzle, and there is *almost* a storyline, so it might even seem like you are playing a game!

Then there are a range of modes designed to interact with Jupyter notebooks that we've created. The tutorial will guide you to create your own program to solve a real problem, and the notebooks will allow you to run these programs on a real quantum computer.

Current supported modes are as follows.

* **Image Superposer**: Create quantum superpositions of images with the notebook [here](https://github.com/decodoku/Quantum_Programming_Tutorial/tree/master/image-superposer).

More are coming soon.

There is also the **Sandbox Mode**, which let's you try out all the skills learned in the puzzles.

## How to use

Start by downloading this repository using [this link](https://github.com/decodoku/Quantum_Programming_Tutorial/archive/master.zip) and unzipping it.

If you have a Mac, you can simomply run the file *QuantumProgrammingTutorial* found inside. You should need to change your security settings to allow it to run *(note: running executables from the internet is not a great idea in general)*. If you prefer to compile yourself, you can do this using the Xcode project found in the folder.

To complile on Linux, you'll need to [install Swift](https://swift.org/getting-started/#installing-swift). Then dowmload this repository and navigate to

``` Quantum_Programming_Tutorial-master/Hello\ Quantum/Hello\ Quantum```

then use the following commands to compile and run.

```
swiftc StringCommandLineColorExtension.swift Shrink.swift main.swift
./main
```
For Windows, no way of compiling the Swift source codes has been tested. It might be possible, but we just don't know.

The program runs on the command line. For best results, you should maximize the size of your command line window. If you need to change font and background settings, you can use the `⌘,` shortcut on Mac. The *Basic* profile with Menlo 11pt font and white background work well.

## What next?

For some discussion of what is being done in the tutorial, check out the following articles.
* [Visualizing bits and qubits](https://medium.com/qiskitters/visualizing-bits-and-qubits-9af287047b28)

Once you have mastered this gamified tutorial, you will be writing the kind of quantum programs found in the [tutorial for the QISKit SDK](https://github.com/QISKit/qiskit-tutorial). So head there to find more inspiration.

## Credits

This project was a collaboration between James R. Wootton at the University of Basel and some supporters of QISKit.
