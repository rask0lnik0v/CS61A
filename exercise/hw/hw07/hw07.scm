(define (filter-lst fn lst)
  'YOUR-CODE-HERE
  (cond ((equal? lst nil) nil)
    	((fn (car lst)) 
	 (cons (car lst) (filter-lst fn (cdr lst)))
	 )
    	(else (filter-lst fn (cdr lst)))
  )
    
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (interleave first second)
  'YOUR-CODE-HERE
  (define (inter_helper first second index)
     (cond ((and (equal? first nil) (equal? second nil))
		nil
	   )

	   ((equal? first nil)
		(cons (car second) (inter_helper first (cdr second) 1))
	   )

	   ((equal? second nil)
		(cons (car first) (inter_helper (cdr first) second 0))
	   )

	   (else
	     (if (= index 0)
		(cons (car first) (inter_helper (cdr first) second 1))
		(cons (car second) (inter_helper first (cdr second) 0))
	     )
	   )
    )   
  )

  (inter_helper first second 0)
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (define (helper combiner start n term index)
  (cond ((= n 0)
	 (term index)
	)
	((= index 0)
	 (combiner start (helper combiner start (- n 1) term (+ index 1)))
	)
	(else
	  (combiner (term index) (helper combiner start (- n 1) term (+ index 1)))
	)
      
  )
  )

  (helper combiner start n term 0)
)


(define (no-repeats lst)
  'YOUR-CODE-HERE
  (cond ((null? lst) nil)
	(else (cons (car lst)
		    (no-repeats
		      (filter (lambda (x) (not (= (car lst) x))) (cdr lst) )))))
)

