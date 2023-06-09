use std::fs;

fn main() {
    let fp = "./inputs/p01";
    let contents = fs::read_to_string(fp)
        .expect("Should have been able to read this file");
    let mut count = 0;
    for c in contents.chars() {
        match c {
            '(' => count += 1,
            ')' => count -= 1,
            _ => (),
        }
    }
    println!("Number of stairs: {}", count);

    count = 0;
    for (i, c) in contents.char_indices() {
        match c {
            '(' => count += 1,
            ')' => count -= 1,
            _ => (),
        }
        if count == -1 {
            println!("Basement at index: {}", i+1)
        }
    }
}
