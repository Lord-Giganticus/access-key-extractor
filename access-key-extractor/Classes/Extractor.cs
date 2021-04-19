using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace access_key_extractor.Classes
{
    internal class Extractor
    {
        internal static string RunExtractor(FileInfo file)
        {
            var startinfo = new ProcessStartInfo
            {
                FileName = "node.exe",
                Arguments = $"extractor {file.FullName}",
                UseShellExecute = false,
                RedirectStandardOutput = true,
                CreateNoWindow = true
            };
            var lines = new List<string>();
            var process = new Process
            {
                StartInfo = startinfo
            };
            process.Start();
            while (!process.HasExited)
                if (!process.HasExited)
                    lines.Add(process.StandardOutput.ReadLine());
                else
                    break;
            if (lines[1] is "No possible access keys found")
                throw new Exception("No possible access keys found.");
            else
                return lines[3];
        }
    }
}
