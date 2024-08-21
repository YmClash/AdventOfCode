use ymcrust::{read_file,};



fn main() {
    println!("Hello, world!");

    let file = r"C:\Users\y_mc\RustroverProjects\AdventOfCode\Ad_Of_C_2015\RUST\Day_2\src\test.txt";
    let puzzle = read_file(file);
    let puzzle = puzzle.unwrap();
    println!("Bienvenue a Advent of Code 2015");
    println!("Puzzle # 2");
    println!("Longeur du puzzle: {}",puzzle.lines().count());

    let mut paperdim:Vec<i32> = Vec::new();

/////////////////////////////////////////////////////////////////////
    // for i in 0..puzzle.lines().count() {
    //     let mut _dim: Vec<i32> = Vec::new();
    //     for line in puzzle.lines() {
    //         for word in line.split('x') {
    //             let word = word.parse::<i32>().unwrap();
    //             _dim.push(word);
    //             println!("Dimension: {:?}", _dim);
    //         }
    //
    //     }
    // }
////////////////////////////////////////////////////////////
    // }
    // for line in puzzle.lines(){
    //     let _dim:Vec<i32> = Vec::new();
    //     for word in line.split('x'){
    //         let word = word.parse::<i32>().unwrap();
    //         paperdim.push(word);
    //     }
    //     println!("Dimension: {:?}",_dim);
    // }




    for line in puzzle.lines(){
        for word in line.split('x'){
            let word = word.parse::<i32>().unwrap();
            paperdim.push(word);
        }
    }

    println!("Dimension: {:?}",paperdim);
    let smallest = smallest_side(paperdim[0],paperdim[1],paperdim[2]);
    let surface = surface_area(paperdim[0],paperdim[1],paperdim[2]);
    let total = surface + smallest;

    println!("Surface: {}",surface);
    println!("Smallest Side : {}",smallest);
    println!("Total: {}",total);





}

fn surface_area(longueur:i32, largeur:i32, hauteur:i32) -> i32{
    let surface = 2*longueur*largeur + 2*largeur*hauteur + 2*hauteur*longueur;
    return surface
}

fn smallest_side(longueur:i32, larger:i32, hauteur:i32) -> i32{
    let mut side = longueur* larger;
    if side > larger *hauteur{
        side = larger *hauteur;
    }else if side > hauteur*longueur{
        side = hauteur*longueur;
    }
    return side;
}

/*
Dimension #1 : [29, 13, 26]
smallest side : 338
Surface: 2938 + 338 = 3276
Surface Ruban: 78 + 9802 = 9880

Dimension #2 : [29, 13, 26]
smallest side : 338
Surface: 2938 + 338 = 3276
Surface Ruban: 78 + 9802 = 9880
*/