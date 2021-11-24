(ns clojure-leetcode.problem_1812)

; creating a hash map of the letters
(def letters-odd [\a \c \e \g])

(defn squareIsWhite [coordinate] 
  (= 
    ; we check if the letter is an odd letter
    (.contains letters-odd (get coordinate 0)) 
    ; we check if the number is an odd number
    ; we have to do some type casting since `get coordinate`
    ; returns a Character even though we want a digit
    (= (mod (Character/digit (get coordinate 1) 10) 2) 0) 
    )
  )

; defining the test case function
(defn testCase [function input output]
  (if (= (function input) output)
    (println "Success")
    (println "Failure")
    )
  )

; running the function
(testCase squareIsWhite "a1" false)
(testCase squareIsWhite "h3" true)
(testCase squareIsWhite "c7" false)
