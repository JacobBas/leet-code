// * A simple CLI tool for initializing a new questions structure
// * by creating the folder and populating it with the initial python
// * script. Further enhancements are going to be to create init scripts
// * for other languages such as go, rust, and c++.

// * it might also be worthwhile to rewrite this within a different langauge
// * since this executable file is 1.9MB large for very simple functionality.

package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

const init_py = `import unittest


class Tests(unittest.TestCase):
	def mainFunction(self, input: type) -> type:
		pass

	def test1(self):
		input = '<input>'
		output = '<output'
		self.assertEqual(
			self.mainFunction(input),
			output,
		)


if __name__ == '__main__':
	unittest.main()
`

func main() {
	// handling if no argument is given to the command
	if len(os.Args) < 2 {
		panic("please enter a question number")
	}

	// pulling out the question number
	qNum := os.Args[1]
	qLen := len(qNum)
	zerosLen := 4 - qLen

	// handling if the question can be converted to an int
	_, err := strconv.Atoi(qNum)
	if err != nil {
		panic("please enter a valid integer value")
	}

	// handling if the question number is not valid
	if qLen > 4 {
		panic("question can be no longer than 4 characters")
	}

	// defining the folder name
	qNum = "_q_" + strings.Repeat("0", zerosLen) + qNum

	// checking if the folder already exists
	_, err = os.Stat(qNum)
	if !os.IsNotExist(err) {
		panic("this question's folder already exists")
	}

	// creating the new folder
	err = os.Mkdir(qNum, 0777)
	if err != nil {
		panic("something went wrong while creating the folder")
	}

	// initializing the main.py file
	fileName := qNum + "/main.py"
	f, err := os.OpenFile(fileName, os.O_CREATE|os.O_WRONLY, 0777)
	if err != nil {
		panic("something went wrong while creating the python file")
	}
	defer f.Close()

	// writing to the main.py file
	_, err = f.WriteString(init_py)
	if err != nil {
		fmt.Println(err)
		panic("something went wrong while creating the python file")
	}
}