using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace access_key_extractor.Classes
{
    internal class JSON
    {
        internal static void Serialize(object data, string filePath)
        {
            var serializer = new JsonSerializer();

            using var sw = new StreamWriter(filePath);
            using JsonWriter writer = new JsonTextWriter(sw)
            {
                Formatting = Formatting.Indented
            };
            serializer.Serialize(writer, data);
        }

        internal static object Deserialize(string path)
        {
            var serializer = new JsonSerializer();

            using var sw = new StreamReader(path);
            using var reader = new JsonTextReader(sw);
            return serializer.Deserialize(reader);
        }

        internal static Task SerializeAsync(object data, string filePath)
        {
            return Task.Run(() => Serialize(data, filePath));
        }

        internal static Task<object> DeserializeAsync(string path)
        {
            return Task.Run(() => Deserialize(path));
        }
    }
}
