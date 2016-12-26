using System;
using System.Collections.Generic;
using System.IO;
class Solution {
        static void Main(string[] args)
        {
            int c = int.Parse(Console.ReadLine());
            List<UInt32> lst = new List<uint>();
            for (int i = 0; i < c; i++)
            {
                UInt32 ui = UInt32.Parse(Console.ReadLine());
                lst.Add(~ui);
            }
            
            lst.ForEach(Console.WriteLine);
        }

}