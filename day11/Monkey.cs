public class Monkey
{
    public List<int> items { get; set; }
    public string op_type { get; set; }
    public int op_value { get; set; }
    public int test_div_value { get; set; }
    public int test_true_monkey { get; set; }
    public int test_false_monkey { get; set; }
    public int inspections { get; set; }

    public static int UpdateWorry(int worry, string op, int value)
    {
        if (value == -1)
            worry *= worry;
        else if (op == '*')
            worry *= value;
        else if (op == '+')
            worry += value;

        //worry = worry // 3
        return worry;
    }
}