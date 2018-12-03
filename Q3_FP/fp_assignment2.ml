let rec unparse (ast : Syntax.t) =
  match ast with
  (* simple exp *)
  | Syntax.Unit -> "()"
  | Syntax.Bool e-> string_of_bool e
  | Syntax.Int n -> string_of_int n
  | Syntax.Float n -> string_of_float n
  | Syntax.Var v -> v
  | Syntax.Get(e1,e2) -> unparse e1^".("^unparse e2^")"
  | Syntax.Put(e1,e2,e3) -> unparse e1 ^ ".(" ^ unparse e2 ^ ") <-" ^ unparse e3
 (* exp *)
 (*  | Syntax.Not e -> "(not " ^ unparse e ^ ")" *)
  | Syntax.Neg e -> " - "^ unparse e
  | Syntax.FNeg e -> " -. "^ unparse e
  (* +-*/ *)
  | Syntax.Add(e1,e2) -> "(" ^ unparse e1 ^ " + " ^ unparse e2 ^ ")"
  | Syntax.FAdd(e1,e2) -> "(" ^  unparse e1 ^ " +. " ^ unparse e2 ^ ")"
  | Syntax.Sub(e1,e2) -> "(" ^ unparse e1 ^ " - " ^ unparse e2 ^ ")"
  | Syntax.FSub(e1,e2) -> "(" ^  unparse e1 ^ " -. " ^ unparse e2 ^ ")"
  | Syntax.Eq(e1, e2) -> "(" ^ unparse e1 ^ " = " ^ unparse e2 ^ ")"
  | Syntax.FMul(e1,e2) -> "(" ^ unparse e1 ^ " *. " ^ unparse e2 ^ ")"
  | Syntax.FDiv(e1,e2) -> "(" ^ unparse e1 ^ " /. " ^ unparse e2 ^ ")"
  (* less_greater; less; greater ; not*)
  | Syntax.Not e -> 
        (match e with
          | Syntax.Eq(e1,e2) -> "(" ^ unparse e1 ^ " <> " ^ unparse e2 ^ ")"
          | Syntax.LE(e1,e2) -> "(" ^ unparse e1 ^ " > " ^ unparse e2 ^ ")"
          | _ -> "(not " ^ unparse e ^ ")")
  (* less_eq or greater_eq *)
  | Syntax.LE(e1,e2) -> "(" ^ unparse e2 ^ " >= " ^ unparse e1 ^ ")"
  | Syntax.If(e1,e2,e3) -> "if " ^ unparse e1 ^ " then " ^ 
      unparse e2 ^ " else " ^ unparse e3
   (* Let of (Id.t * Type.t) * t * t*)
  | Syntax.Let((id,ty),e1,e2) ->  
        (match ty with
          | Unit -> unparse e1 ^ " ; " ^ unparse e2
          |_ -> "let " ^ id ^ " = " ^ unparse e1 ^ " in " ^ unparse e2)
  | Syntax.App(f, args) ->
        (match unparse f with
          | "print_newline" -> "print_newline()" 
          | _ -> (unparse f) ^ "(" ^ String.concat " " (List.map unparse args) ^ ")" )
  | Syntax.Tuple args -> "(" ^ String.concat ", " (List.map unparse args) ^ ")"
  | Syntax.LetTuple(args,e1,e2) -> 
      "let (" ^ String.concat ", " (List.map (function n -> (match n with | (id,ty) -> id)) args) 
      ^ ") = " ^ unparse e1 ^ " in " ^ unparse e2
  | Syntax.Array(e1,e2) -> "Array.make " ^ unparse e1 ^ " " ^ unparse e2
  | Syntax.LetRec(fundef,e) -> 
      "let rec " ^ (match fundef with
        | {name;args;body} -> (match name with | (id,ty) -> id) ^ " " ^
        (String.concat " " (List.map (function n -> (match n with | (id,ty) -> id)) args) ) ^ " = "
        ^ unparse body
      ) ^ " in " ^ unparse e ;;