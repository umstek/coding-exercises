Module Module1

    Sub Main()
        Console.ReadLine()
        Dim inp As String() = Console.ReadLine().Trim().Split()
        Array.Reverse(inp)
        Console.WriteLine(String.Join(" ", inp))
    End Sub

End Module
