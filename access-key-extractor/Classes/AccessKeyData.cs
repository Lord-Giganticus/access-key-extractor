using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace access_key_extractor.Classes
{
    internal class AccessKeyData
    {
        public AccessKeyData(FileInfo file, string keys)
        {
            Name = Path.GetFileNameWithoutExtension(file.FullName);
            Keys = keys;
        }

        public string Name { get; set; }

        public string Keys { get; set; }
    }
}
