﻿using System;
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
        internal static event NotifyExtractor Complete;

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
            try
            {
                Complete?.Invoke();
                return lines[3];
            }
            catch
            {
                throw new Exception("No possible access keys found.");
            } 
        }

        internal static Task<string> RunExtractorAsync(FileInfo file)
        {
            return Task.Run(() => RunExtractor(file));
        }

        internal delegate void NotifyExtractor();
    }
}
