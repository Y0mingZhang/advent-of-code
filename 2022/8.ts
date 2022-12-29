import fs from "fs";


const data: string = fs.readFileSync("../data/8.in", "utf8")
const grid = data.split('\n').map(x => x.split('').map(Number));

class Node<T> {
    val?: T;
    prev: Node<T> | null;
    next: Node<T> | null;

    constructor(
        val?: T,
        prev: Node<T> | null = null,
        next: Node<T> | null = null) {
        this.val = val;
        this.prev = prev;
        this.next = next;
    }

    prettyPrint(): string {
        if (this.next === null) {
            return String(this.val);
        }
        return String(this.val) + ' -> ' + this.next.prettyPrint();
    }
}

class Stack<T> {
    private head: Node<T>
    private tail: Node<T>

    constructor() {
        this.head = new Node();
        this.tail = new Node();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    empty(): boolean {
        return this.head.next === this.tail;
    }

    top(): T {
        if (this.tail.prev === null || this.tail.prev.val === undefined) {
            throw Error;
        }
        return this.tail.prev.val;
    }

    push(val: T): void {
        const node = new Node(val, this.tail.prev, this.tail);
        if (node.prev === null) {
            throw Error;
        }
        node.prev.next = node;
        this.tail.prev = node;
    }

    pop(): T {
        const node = this.tail.prev;
        if (node === null || node.prev === null || node.val == undefined) {
            throw Error;
        }
        node.prev.next = this.tail;
        this.tail.prev = node.prev;
        return node.val;
    }

    prettyPrint(): string {
        return this.head.prettyPrint();
    }

}


function hflip(arr: number[][]): number[][] {
    return arr.map(
        row => row.map((_, i) => row[row.length - 1 - i])
    );
}

function transpose(arr: number[][]): number[][] {
    const N = arr[0].length;
    return [...Array(N).keys()].map(
        j => arr.map(
            (_, i) => arr[i][j]
        )
    );
}

function multiply(x: number[][], y: number[][]): number[][] {
    return x.map(
        (row, i) => row.map(
            (_, j) => x[i][j] * y[i][j]
        )
    );
}

function invisible(arr: number[]): number[] {
    const res = new Array<number>;
    let maxSeen = -1;

    for (const x of arr) {
        res.push(x <= maxSeen ? 1 : 0);
        maxSeen = Math.max(maxSeen, x);
    }
    return res;
}

function leftScore(arr: number[]): number[] {

    const monoStk = new Stack<number>;
    const res = new Array<number>;

    for (let i = 0; i < arr.length; ++i) {
        while (!monoStk.empty() && arr[monoStk.top()] < arr[i]) {
            monoStk.pop();
        }
        if (monoStk.empty()) {
            res.push(i);
        } else {
            res.push(i - monoStk.top());
        }
        monoStk.push(i);
    }
    return res;
}

function invisibles(arr: number[][]): number[][] {
    return arr.map(invisible);
}

function scores(arr: number[][]): number[][] {
    return arr.map(leftScore);
}

function part1(): number {
    const gridT = transpose(grid);
    const scoreL = invisibles(grid);
    const scoreR = hflip(invisibles(hflip(grid)));
    const scoreU = transpose(invisibles(gridT));
    const scoreD = transpose(hflip(invisibles(hflip(gridT))));
    const score = multiply(multiply(scoreL, scoreR), multiply(scoreU, scoreD));
    return score.flat().reduce(((acc, val) => val == 0 ? acc + 1 : acc), 0);
}

function part2(): number {
    const gridT = transpose(grid);
    const scoreL = scores(grid);
    const scoreR = hflip(scores(hflip(grid)));
    const scoreU = transpose(scores(gridT));
    const scoreD = transpose(hflip(scores(hflip(gridT))));
    const score = multiply(multiply(scoreL, scoreR), multiply(scoreU, scoreD));
    return Math.max(...score.flat());
}

console.log("part1: ", part1());
console.log("part2: ", part2());