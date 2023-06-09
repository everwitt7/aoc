use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn calc_dims(dims: &String) -> i32 {
    let parts: Vec<i32> = dims
        .split("x")
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    let mut min = i32::MAX;
    let mut res = 0;
    // println!("{:?}", parts);

    for i in 0..parts.len() {
        for j in i+1..parts.len() {
            let prod = parts[i] * parts[j];
            res += 2 * prod;
            if min > prod {
                min = prod;
            }
        }
    }
    // println!("{}", min);
    return res + min;
}
fn main() {
    let fp = "./inputs/p02";
    
    // we have a vector of the input strings, we need to apply a function (map) to the elements
    let lines = read_lines(fp);
    
    let res: Vec<i32> = lines
        .iter()
        .map(calc_dims)
        .collect();

    let ans: i32 = res.iter().sum();
    println!("{}", ans);

    // create test cases for my functions in the future in order to test the samples
    // and then be able to test that via the command line.
    // I also need to attach an LSP and debugger
    let sample: String = String::from("2x3x4");
    let test: i32 = calc_dims(&sample);
    println!("{}", test);
}

