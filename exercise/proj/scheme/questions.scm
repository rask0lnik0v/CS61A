(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
	(list (map car pairs) (map cadr pairs))
)

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  ; 很妙的尾递归方法 
  (define (enumerate_helper s num res)
	(if (null? s)
	     res
	     (enumerate_helper (cdr s) (+ 1 num) 
			       (append res (list (list num (car s))))
	     )
         
	  
        )
  )
  (enumerate_helper s 0 nil)
)
  
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16


  (cond ((null? list1) list2)
	((null? list2) list1)
    	((comp (car list1) (car list2)) (cons (car list1) (cons (car list2) (merge comp (cdr list1) (cdr list2)))))
	(else (cons (car list2) (cons (car list1) (merge comp (cdr list1) (cdr list2)))))
    )

 


)
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (if (null? s)
      	nil
	(let ((rest (nondecreaselist (cdr s)) ))
	 (if (or (null? (cdr s)) (> (car s) (cadr s)))
	 	(cons (list (car s)) rest)
	 	(cons (cons (car s) (car rest)) (cdr rest))
	  )
	 )
      )
 )
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr 
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
	 expr
	 ; quote与原子情况直接返回即可
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
	   (cons form (cons params (let-to-lambda body)))
	   ; lambda表达式需要判断其body有没有let，所以继续递归
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
	   (define combine (zip values))
	   ; 首先定义combine，对于((a 1) (b 2))，就是((a b) (1 2))
	   (cons (cons 'lambda (cons (let-to-lambda (car combine)) (cons (let-to-lambda (car body)) nil))) (map let-to-lambda (cadr combine)))
	   ; 前半部分是lambda表达式的本体部分，标准的用scheme的list重写了一遍 
	   ; 后半部分是值，使用map对值进行映射
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
	 (cons (car expr) (map let-to-lambda (cdr expr)))
	 ; 其他情况对cdr部分继续进行递归判断
         ; END PROBLEM EC
         )))

