using System;
using System.Collections.Generic;

namespace CSharp
{
    public class ArrayList
    {
        public ArrayList()
        {
            LinkedList<int> a = new LinkedList<int>();

            a.AddAfter(100);
        }

        public static void Main(string[] args)
        {
            Console.WriteLine("Hello CSharp");
        }
    }
}
