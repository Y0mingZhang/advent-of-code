#!/opt/homebrew/bin/elixir

defmodule Main do
  def simulate do
    {:ok, input} = File.read("../data/9.in")

    instructions =
      List.flatten(
        Enum.map(String.split(input, "\n"), fn <<head, _, rest::binary>> ->
          List.duplicate(
            List.to_string([head]),
            elem(Integer.parse(rest), 0)
          )
        end)
      )

    simple_tail_locs = [{0, 0} | move_simple({0, 0}, {0, 0}, instructions)]
    IO.puts("part 1: #{length(Enum.uniq(simple_tail_locs))}")
    complex_tail_locs = [{0, 0} | move_complex({0, 0}, List.duplicate({0, 0}, 9), instructions)]
    IO.puts("part 2: #{length(Enum.uniq(complex_tail_locs))}")
  end

  defp move_simple(head, tail, [dir | rest]) do
    head_new = move_head(head, dir)
    tail_new = move_tail(head_new, tail)
    [tail_new | move_simple(head_new, tail_new, rest)]
  end

  defp move_simple(_, _, []) do
    []
  end

  defp move_complex(head, tails, [dir | rest]) do
    head_new = move_head(head, dir)

    {tails_new, last_tail} =
      Enum.map_reduce(tails, head_new, fn t, h -> {move_tail(h, t), move_tail(h, t)} end)

    [last_tail | move_complex(head_new, tails_new, rest)]
  end

  defp move_complex(_, _, []) do
    []
  end

  defp move_head({head_x, head_y}, dir) do
    case dir do
      "U" -> {head_x, head_y + 1}
      "D" -> {head_x, head_y - 1}
      "R" -> {head_x + 1, head_y}
      "L" -> {head_x - 1, head_y}
    end
  end

  defp move_tail({head_x, head_y}, {tail_x, tail_y}) do
    if (head_x - tail_x) ** 2 + (head_y - tail_y) ** 2 > 2 do
      {round(head_x * 2 / 3 + tail_x / 3), round(head_y * 2 / 3 + tail_y / 3)}
    else
      {tail_x, tail_y}
    end
  end
end

Main.simulate()
