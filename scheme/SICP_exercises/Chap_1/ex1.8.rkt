#lang racket

;; Newton's method to get cube root

(define (cube-iter guess x)
  (if (good-enough? guess x)
      guess
      (cube-iter (improve guess x) x)))

;; 
(define (improve guess x)
  (average (/ x (* guess guess))
           (* 2 guess)))

(define (average x y)
  (/ (+ x y)
     3))

(define (good-enough? guess x)
  (< (/ (abs (- (* guess guess guess)
             x))
        x)
     0.001))
;; main function of my-cube
(define (my-cube x)
  (cube-iter 1.0 x))

;; for test
(my-cube 27)
(my-cube 1e9)
(my-cube 1e-9)