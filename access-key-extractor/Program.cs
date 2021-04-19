using System;
using System.Collections.Generic;
using System.IO;
using access_key_extractor.Properties;
using access_key_extractor.Classes;
using System.Threading.Tasks;

namespace access_key_extractor
{
    internal class Program
    {
        internal static void Main() =>
            MainAsync().GetAwaiter().GetResult();

        protected internal static async Task MainAsync()
        {
            if (!File.Exists("wiiurpxtool.exe"))
                await File.WriteAllBytesAsync("wiiurpxtool.exe", Resources.wiiurpxtool);
            if (!File.Exists("extractor.js"))
                await File.WriteAllTextAsync("extractor.js", Resources.extractor);
            if (!Directory.Exists("temp"))
                Directory.CreateDirectory("temp");
            var dir = new DirectoryInfo(Directory.GetCurrentDirectory());
            var rpx_files = new List<FileInfo>();
            foreach (var file in dir.GetFiles())
                if (file.Extension is ".rpx")
                    rpx_files.Add(file);
            await Wiiurpxtool.RunWiiurpxtoolAysnc(rpx_files);
            foreach (var file in rpx_files)
            {
                File.Move(file.FullName, $"temp/{file.Name}");
            }
            foreach (var file in dir.GetFiles())
                if (file.Extension is ".elf")
                {
                    var Data = new AccessKeyData(file, Extractor.RunExtractor(file));
                    await JSON.SerializeAsync(Data, $"{Path.GetFileNameWithoutExtension(file.FullName)}-key.json");
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