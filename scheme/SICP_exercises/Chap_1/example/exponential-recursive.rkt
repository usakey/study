#lang racket

;; linear recursive process
(define (expt b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))

;; test
(expt 2 3)