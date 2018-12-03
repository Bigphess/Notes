
(* Q1 *)
(*float number*)
let volume_of_cube a =
  if a <= 0. then raise (Failure"not a cube")
  else a*.a*.a
;;


(* Q2 *)
(*cube root*)
let edgelen_of_cube volume =
	if volume <= 0. then raise (Failure "not a cube")
    else volume**(1./.3.)
;;

(* Q3 *)
(*is the list empty? list.map*)
let volumes_of_cubes edgelens =
  if hd edgelens >0.
   then List.map (volume_of_cube) edgelens
   (*but have already make sure data is bigger than 0 *)
  else failwith "data is wrong, not cubes"

and  hd edgelens =
    match edgelens with
    hd::rest->hd
   | _-> failwith "you didn't enter the data"
;;

(* Q4 *)
(*type number = Int of int | Float of float | Error;;
type sign = Positive | Negative;;

let sign_int n =
  if n >= 0 then Positive
  else Negative;;

let div_num n1 n2 =
  Error;;*)

let rec ack m n =
  if m == 0 then n+1
  else if m > 0 && n = 0 then ack (m - 1) n
  else if m > 0 && n > 0 then ack (m - 1) (ack m (n - 1))
  else failwith "input error" 
  ;; 

(* Note: div_num (Int 4) (Int 2) should give (Int 2) rather than (Float 2.0) *)


(*Q5*)
(*compare inner function counter*)
let wc words word =
 let rec inner count words word =
  match words with
  | [] -> count
  | hd :: the_rest -> 
  if (compare hd word == 0) then inner (count+1) the_rest word
  else  inner count the_rest word
 in 
 inner 0 words word
  ;;
