using System;
using System.Collections.Generic;
using System.IO;
using access_key_extractor.Properties;
using access_key_extractor.Classes;

namespace access_key_extractor
{
    class Program
    {
        static void Main()
        {
            if (!File.Exists("wiiurpxtool.exe"))
                File.WriteAllBytes("wiiurpxtool.exe", Resources.wiiurpxtool);
            if (!File.Exists("extractor.js"))
                File.WriteAllText("extractor.js", Resources.extractor);
            if (!Directory.Exists("temp"))
                Directory.CreateDirectory("temp");
            var dir = new DirectoryInfo(Directory.GetCurrentDirectory());
            var rpx_files = new List<FileInfo>();
            foreach (var file in dir.GetFiles())
                if (file.Extension is ".rpx")
                    rpx_files.Add(file);
            Wiiurpxtool.RunWiiurpxtool(rpx_files);
            foreach (var file in rpx_files)
            {
                File.Move(file.FullName, $"temp/{file.Name}");
            }
            foreach (var file in dir.GetFiles())
                if (file.Extension is ".elf")
                {
                    var Data = new AccessKeyData(file, Extractor.RunExtractor(file));
                    JSON.Serialize(Data, $"{Path.GetFileNameWithoutExtension(file.FullName)}-key.json");
                    file.Delete();
                }
            Directory.SetCurrentDirectory("temp");
            var temp_dir = new DirectoryInfo(Directory.GetCurrentDirectory());
            foreach (var file in temp_dir.GetFiles())
                File.Move(file.FullName, $"{dir.FullName}/{file.Name}");
            Directory.SetCurrentDirectory(dir.FullName);
            Directory.Delete("temp");
            Console.WriteLine("Complete. Press any key to exit.");
            Console.ReadKey();
        }
    }
}