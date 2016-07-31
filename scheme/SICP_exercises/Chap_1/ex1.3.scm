#lang racket

;; Define a procedure that takes three numbers
;; as arguments and returns the sum of the squares of the two
;; larger numbers.

(define (sum_of_square x y)
  (+ (* x x)
     (* y y)))
;; find the mimimum of three
(define (large_sum_square x y z)
  (cond ((and (>= x z)
              (>= y z))
         (sum_of_square x y))
        ((and (>= y x)
              (>= z x))
         (sum_of_square y z))
        ((and (>= x y)
              (>= z y))
         (sum_of_square x z))))


;; for test
(large_sum_square 2 2 2)