use ymcrust::{ read_file,read_file_length};



fn count_etage(puzzle: &str) -> i32 {
    let mut etage = 0 ;
    for c in puzzle.chars() {
        if c == '(' {
            etage += 1;
        } else if c == ')' {
            etage -= 1;
        }
    }
    return etage;
}

fn position_etage(puzzle:&str) -> Vec<i32>{
    let mut floor = Vec::new();
    for c in puzzle.chars(){
        if c == '(' {
            floor.push(1);
        } else if c == ')' {
            floor.push(-1);
        }
    }
    return floor;
}




fn main() {
    let file = r"C:\Users\y_mc\RustroverProjects\AdventOfCode\Ad_Of_C_2015\RUST\Day_1\src\input.txt";
    let puzzle = read_file(file);
    let puzzle = puzzle.unwrap();
    println!("Bienvenue a Advent of Code 2015");
    println!("Puzzle # 1");
    println!("Longeur du puzzle: {}",puzzle.len());
    println!("Longeur du puzzle: {}",read_file_length(file));
    println!("Puzzle #1A: To what floor do the instructions take Santa?");

    let resultat = count_etage(&puzzle);
    println!("Resultat: {}",resultat);

    println!("Puzzle #1B: What is the position of the character that causes Santa to first enter the basement?");
    let resultat_2  = position_etage(&puzzle);
    //println!("Resultat 2: {:?}",resultat_2);

    let mut position = 0;
    let mut etage = 0;
    for (i, &item) in resultat_2.iter().enumerate(){
        etage += item;
        if etage == -1 {
            position = i + 1;
            break;
        }
    }

    println!("Resultat 2: {}",position);



    println!("Done");

    println!("Code by YmC");








    //
    //
    // let test_1 = "(())";    //0
    // let test_2 = "(()(()("; //3
    // let test_3 = "))(";    //-1
    // let test_4 = ")())())";    //
    //
    // let resultat_ = count_etage(test_1);
    // let resultat_2 = count_etage(test_2);
    // let resultat_3 = count_etage(test_3);
    // let resultat_4 = count_etage(test_4);
    // println!("Resultat test 1: {} Etage", resultat_);
    // println!("Resultat test 2: {} Etage", resultat_2);
    // println!("Resultat test 3: {} Etage", count_etage(test_3));
    // println!("Resultat test 4: {} Etage", count_etage(test_4));



}


