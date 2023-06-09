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

fn calc_ribbons(dims: &String) -> i32 {
    let mut parts: Vec<i32> = dims
        .split("x")
        .map(|s| s.parse::<i32>().unwrap())
        .collect();

    parts.sort(); 

    let mut res = 1;
    for i in 0..parts.len() {
        res *= parts[i]
    }

    let perim = 2 * parts[0] + 2 * parts[1];
    
    // println!("{}, {}", perim, res);
    return perim + res;
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


    // part 2
    let rib_res: Vec<i32> = lines
        .iter()
        .map(calc_ribbons)
        .collect();

    let rib_ans: i32 = rib_res.iter().sum();
    println!("{}", rib_ans);



    // create test cases for my functions in the future in order to test the samples
    // and then be able to test that via the command line.
    // I also need to attach an LSP and debugger
    let sample: String = String::from("2x3x4");
    let test: i32 = calc_dims(&sample);
    println!("{}", test);

    let rib_test: i32 = calc_ribbons(&sample);
    println!("{}", rib_test);
}

