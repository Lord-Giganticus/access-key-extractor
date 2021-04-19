using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace access_key_extractor.Classes
{
    internal class Wiiurpxtool
    {
        internal static void RunWiiurpxtool(List<FileInfo> files)
        {
            foreach (var file in files)
            {
                var startinfo = new ProcessStartInfo
                {
                    FileName = "wiiurpxtool.exe",
                    Arguments = $"-d {file.FullName} {Path.GetFileNameWithoutExtension(file.FullName)}.elf",
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    CreateNoWindow = true
                };
                Process.Start(startinfo).WaitForExit();
            }
        }

        internal static Task RunWiiurpxtoolAysnc(List<FileInfo> files)
        {
            return Task.Run(() => RunWiiurpxtool(files));
        }
    }
}
