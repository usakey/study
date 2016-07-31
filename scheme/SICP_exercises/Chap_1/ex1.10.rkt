#lang racket

;; Ackermann’s function
(define (A x y)
  (cond ((= y 0) 0)
        ((= x 0) (* 2 y))
        ((= y 1) 2)
        (else (A (- x 1) (A x (- y 1))))))

;; test
(A 1 10) ;; 2^10
(A 2 4)  ;; 2^2^2^2 = 2^16 = 65536
(A 3 3)  ;; 65536 


;; A(0, n) = 2 * n
;; A(1, n) = 2 ^ n
;; A(2, n) = 2 ^ 2 ^ 2...^2 (n 2)
(define (f n) (A 0 n))
(define (g n) (A 1 n))
(define (h n) (A 2 n))

;; test
(f 3) ; 6
(g 3) ; 8
(h 3) ; 16