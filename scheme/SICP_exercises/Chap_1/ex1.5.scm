#lang racket

;; to test interpreter is
;; applicative-order or
;; normal-order

(define (p) (p))
(define (test x y)
  (if (= x 0) 0 y))

;; test
;; as Scheme is applicative-order
;; which means to evaluate firstly
;; the program will be in infinite-loop
(test 0 (p))
