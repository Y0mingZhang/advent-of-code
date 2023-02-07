#!/opt/homebrew/bin/crystal

cycle = 0
x = 1
x_arr = [1]

File.read_lines("../data/10.in").each do |line|
    command = line[0..3]
    if command == "noop"
        x_arr << x
    elsif command == "addx"
        x_arr << x
        var = line[5..].to_i
        x += var
        x_arr << x
    end
end

part_1_indices = [20, 60, 100, 140, 180, 220]
part_1 = 0

part_1_indices.each do |idx|
    part_1 += x_arr[idx - 1] * idx
end

puts("Part 1: " + part_1.to_s)

crt_str = ""
(0...x_arr.size - 1).each do |idx|
    crt_idx = idx % 40
    if (x_arr[idx] - crt_idx).abs <= 1
        crt_str = crt_str + '#'
    else
        crt_str = crt_str + '.'
    end

    if crt_idx == 39
        crt_str = crt_str + '\n'
    end
end

puts("Part 2:", crt_str)