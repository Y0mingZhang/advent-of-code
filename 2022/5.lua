#!/usr/local/bin/lua

function read_data()
    stacks = {}
    procedures = {}

    for i = 1, 9, 1 do
        stacks[i] = {}
    end

    for line in io.lines("../data/5.in") do
        if string.match(line, "]") ~= nil then
            for i = 1, 9, 1 do
                idx = i * 4 - 2
                char = string.sub(line, idx, idx)
                if char ~= " " then
                    table.insert(stacks[i], char)
                end
            end
        elseif string.sub(line, 1, 4) == "move" then
            proc_idx = #procedures + 1
            procedures[proc_idx] = {}
            for w in line:gmatch("%d+") do
                table.insert(procedures[proc_idx], tonumber(w))
            end
        end
    end

    for i = 1, 9, 1 do
        sl = #stacks[i]
        for j = 1, sl // 2, 1 do
            stacks[i][j], stacks[i][sl - j + 1] = stacks[i][sl - j + 1], stacks[i][j]
        end
    end

    return stacks, procedures
end

function partA()
    stacks, procedures = read_data()
    for _, procedure in pairs(procedures) do
        counts = procedure[1]
        from = procedure[2]
        to = procedure[3]
        for _ = 1, counts do
            table.insert(stacks[to], table.remove(stacks[from]))
        end
    end
    io.write("part 1: ")
    for _, stack in pairs(stacks) do
        io.write(stack[#stack])
    end
    io.write('\n')
end

function partB()
    stacks, procedures = read_data()
    for _, procedure in pairs(procedures) do
        counts = procedure[1]
        from = procedure[2]
        to = procedure[3]
        tmp = {}
        for _ = 1, counts do
            table.insert(tmp, table.remove(stacks[from]))
        end
        for _ = 1, counts do
            table.insert(stacks[to], table.remove(tmp))
        end
    end
    io.write("part 2: ")
    for _, stack in pairs(stacks) do
        io.write(stack[#stack])
    end
    io.write('\n')
end

partA()
partB()
