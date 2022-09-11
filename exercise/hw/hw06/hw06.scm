(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s))
)

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cdr (cdr s)))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((equal? num 0) 0)
	((> num 0) 1)
	(else -1)
	)
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (cond ((= x 1) 1)
	((= y 1) x)
	((= (remainder y 2) 1) (* x (pow x (- y 1))))
	(else (square (pow x (/ y 2))))
    )
)

