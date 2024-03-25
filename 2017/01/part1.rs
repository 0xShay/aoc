use std::fs;

fn p1(input: &str) -> i32 {
    let mut res: i32 = 0;
    let mut last_char: char = input.chars().last().unwrap();
    for ch in input.chars() {
        if ch == last_char {
            res += i32::from_str_radix(&String::from(ch), 10).unwrap();
        };
        last_char = ch;
    };
    res
}

fn p2(input: &str) -> i32 {
    let mut res: i32 = 0;
    let offset = input.len() / 2;
    for i in 0..input.len() {
        let ch: char = input.as_bytes()[i] as char;
        let ch_other: char = input.as_bytes()[(i+offset) % input.len()] as char;
        if ch == ch_other {
            res += i32::from_str_radix(&String::from(ch), 10).unwrap();
        };
    };
    res
}

fn main() {
    let input = fs::read_to_string("actual-input.txt").expect("Failed to read file");
    println!("p1: {}", p1(input.as_str()));
    println!("p2: {}", p2(input.as_str()));
}