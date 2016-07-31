#lang racket

;; define new if as procedure
;; here new-if will execute two branches
;; regardless of 
(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))



;; Newton's method to get square root
(define (sqrt-iter guess x)
  (new-if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))

;; 
(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y)
     2))

(define (good-enough? guess x)
  (< (abs (- (* guess guess)
             x))
     0.001))
;; main function of my-sqrt
(define (my-sqrt x)
  (sqrt-iter 1.0 x))

;; for test
(my-sqrt 4)
