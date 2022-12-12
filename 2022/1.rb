
calories = []
curr = 0

File.readlines("../data/1.in").each do |line|
    if line != "\n"
        curr += line.to_i
    else
        calories.push(curr)
        curr = 0
    end
end

calories.sort!.reverse!
puts("top 1 cal", calories[0])
puts("top 3 cal", calories.slice(0, 3).sum)
