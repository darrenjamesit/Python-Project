create database Store_databse;

create table if not exists categories(
    id serial primary key,
    category_name text
)

insert into categories (category_name)
    values
    ('consoles'),
    ('games'),
    ('merchandise'),
    ('accessories');

create table if not exists products(
    id serial primary key,
    name text not null,
    price numeric(10,2),
    description text null,
    stock smallint null,
    category_id int,
    foreign key (category_id)
        references categories(id)
);

create table if not exists images(
    id serial primary key,
    name text,
    img_binarydata bytea,
    prod_id int,
    foreign key (prod_id)
        references products(id)
);

insert into products (name, price, stock, category_id, description)
    values
    ('Aux to Analogue Cable 1.5m', '29.99', '53', '4',
    'Connector: 1 x stereo jack 3.5 mm 4 pin male angled > 3 x male RCA (red, white, yellow). For a portable video camera with stereo jack. Analog audio-video signal. Pin assignment Stereo jack (type > sleeve) ): Audio left - Video - GND - Audio right. Color: black. Length: ca. 1.5 m (incl. connector). System requirements: one free stereo port (video camera) and three free RCA ports (output device)'),
    ('3.5mm Aux Cord 3m', '14.99', '44', '4',
    'This audio cable is an excellent, high-quality construction. Made of galvanized copper and covered with 24 carat gold, it guarantees an impeccable sound. It allows us to connect audio devices in any configuration. It allows you to play your favorite music from your smartphone, laptop, tablet or other sources on any audio device. Connect to a speaker, amplifier or TV and listen to the clear sound, which is guaranteed by the gold-plated plugs.'),
    ('10m High-Speed Ethernet Cable', '19.99', '29', '4',
    'It is used to connect hardware devices in a local network, long life span; RJ45 connectors; Cable length: 10m; the solid connectors offer good resistance to corrosion; the patch cord is the perfect solution for connecting the hardware to the network.'),
    ('4K Gold-Plated HDMI Cable 5m', '49.99', '10', '4',
    'High speed of information transfer, HDMI Ethernet Channel, 24K gold plated connectors for corrosion resistance and superior signal transmission. Supported resolution: ultraHD 4096 x 2160 (4K) pixels, Extended bandwidth - 3D transmission, Superior shielding to reduce electromagnetic interference. Cable length: 5m'),
    ('3.5mm Aux Splitter 0,5m', '17.99', '32', '4',
    'Audio splitter cable Jack 3.5 4-pin female to Jack 3.5 male headphone and Jack 3.5 male microphone, 19cm Uses the Audio Y-cable with Jack 3.5mm, 4-pin (TRRS), female to split the signal into 2 Jack 3.5 3-pin plugs, for Audio, respectively Microphone The product can be used in 2 ways: 1: From laptop with 3.5mm 4-pin jack (Audio + Microphone) to headphones with 3.5mm 3-pin jack + Microphone 3.5mm 3-pin jack 2) From Laptop with 3.5mm 3-pin Jack plug Audio + Jack 3.5 3-pin Microphone in Headset audio Jack 3.5 4-pin (Audio + Microphone) Specifications: Length: 19cm Input: Jack 3.5 - female 4-pin (Audio + Microphone) Output 1: Jack 3.5 - male 3-pin Audio (Green) for headphones, speakers, car aux, etc. Output 2: Jack 3.5 - 3-pin male Microphone (Red) for microphone Connector: Gold-plated'),
    ('USB-A to Type-C Cable (Fast Charge) 3m', '59.99', '88', '4',
    'Durable USB / USB-C cable with nylon ribbon, Fast and safe charging - 2.4A current and pure copper wire provides faster and safer charging. Upload and transfer data at the same time - You can simultaneously upload and transfer data from your phone to your PC. Aluminum connector - High quality aluminum housing, resistant to oxidation and corrosion. Nylon ribbon - the elastic cord has been woven from a strong and durable nylon. '),
    ('VGA-to-VGA Cable 1,5m', '14.99', '7', '4',
    'A double shielded cable with anti-interference coils. Supports HDTV resolution up to 1080.');

insert into products (name, price, stock, category_id, description)
    values
    ('PlayStation 4 500GB', '1999.99', '21', '1',
    'Experience incredibly vivid, vibrant colors with impressive HDR images. Organize your games and applications and share with friends on a new, intuitive interface. Store your games, applications, screenshots and videos with 500 GB and 1 TB options. All the great TV shows and movies, as well as many of your favorite entertainment apps. The DUALSHOCK 4 wireless controller has been updated with a new visual and tactile feel, including a more visible colored light bar, to give you an even bigger part of the game. It is the most ergonomic and intuitive PlayStation controller we have designed so far.'),
    ('PlayStation 5 1TB', '2499.99', '13', '1',
    'The PS5™ console unleashes new gaming possibilities that you never anticipated. Experience lightning-fast loading with an ultra-fast SSD, deeper immersion with haptic feedback compatibility, adaptive triggers and 3D sound, and a new generation of incredible PlayStation® games. Blazing speed - Take advantage of the power of a custom CPU and GPU, as well as the I/O performance of an ultra-fast SSD, which rewrite the rules of what a PlayStation® console can do. Exceptional games - Let yourself be amazed by the incredible graphics and experience the new features of PS5™. Breathtaking Immersion - Discover a deeper gaming experience with support for haptic feedback, adaptive triggers and 3D sound technology. Ultra-fast SSD - Maximize your gaming sessions with near-instant load times for installed PS5™ games. '),
    ('XBox Series X 500GB', '2299.99', '18', '1',
    'Introducing Xbox Series S, the smallest and most elegant Xbox console. Experience the speed and performance of a completely digital last generation console at an affordable price. Start with an instant library of over 100 high-quality games, including all new Xbox Game Studios titles like Halo Infinite on launch day, when you add Xbox Game Pass Ultimate (membership sold separately). Switch seamlessly between multiple games in an instant with Quick Resume. At the heart of the S Series is the Xbox Velocity Architecture, which pairs a custom SSD with integrated software for faster, more streamlined gameplay with significantly reduced load times. '),
    ('Nintendo Switch', '1499.99', '25', '1',
    'The Nintendo Switch system can transform depending on the situation you are in, so you can play your favorite games, no matter how busy you are. Its a new era, where you wont have to change your lifestyle to play - the console will be the one that will change according to your style. Enjoy games anytime, anywhere, with anyone, with flexible and free game modes.'),
    ('Steam Deck 100GB', '1999.99', '7', '1',
    'We partnered with AMD to create Steam Decks custom APU, optimized for handheld gaming. It is a Zen 2 + RDNA 2 powerhouse, delivering more than enough performance to run the latest AAA games in a very efficient power envelope. Your Steam Library, anywhere. Control with comfort. The Steam Deck was built for extended play sessions—whether youre using thumbsticks or trackpads—with full-size controls positioned perfectly within your reach. The rear of the device is sculpted to comfortably fit a wide range of hand sizes.');

insert into products (name, price, stock, category_id, description)
    values
    ('Grand Theft Auto V (GTA 5) Premium Edition PS4', '84.99', '29', '2',
    'Grand Theft Auto V (GTA 5) Premium Edition includes the entire Grand Theft Auto V (GTA 5) experience, the ever-evolving world of Grand Theft Auto V (GTA 5) and all existing gameplay updates and content, including The Doomsday Heist, Gunrunning, Smugglers Run, Bikers and many others.Youll also get the Criminal Enterprise Starter Pack, the fastest way for new GTA Online players to end their criminal empires with the most exciting and popular content, plus a $1,000,000 bonus to spend in GTA online - with a value of 10,000,000 USD.'),
    ('Marvels Spider-Man PS4', '89.99', '5', '2',
    'The most beloved superhero in the world returns in Spider-Man PS4 with all his acrobatic skills, on-the-moment improvisations and his famous spider web that helps him get from one place to another very quickly. The new game awaits you with more parkour, new ways to cross and approach the environment and new combat scenes that will delight any fan.'),
    ('FIFA 23 PS4', '219.99', '49', '2',
    'Experience the pinnacle of international football in FIFA 23 with FIFA World Cup Qatar 2022 and FIFA World Cup Australia and New Zealand 2023.Enjoy the drama and excitement of the biggest sporting tournament as FIFA World Cup comes to FIFA 23 as a post-launch update in November 2022 at no additional cost.Get a seamless tournament experience throughout FIFA 23, with an authentic presentation of the FIFA World Cup, cinematics and all 32 qualified nations in authentic, online, custom and live tournament modes, as well as special content in FIFA 23 Ultimate Team.'),
    ('NBA 2K23 Xbox', '227.99', '11', '2',
    'Compete as your favorite NBA and WNBA teams and stars and experience realistic gameplay. With the best visual presentation yet, improved player AI, updated rosters and historic teams, the game has never felt more real and complete than in NBA 2K. Feel the energy of the crowd, the intensity of the competition and the endless entertainment of one of the most exciting sports products in todays games.'),
    ('Atomic Heart Xbox', '27.99', '108', '2',
    'WHAT IS HIDDEN BEHIND THIS DREAM? The history of the alternate reality of the 1950s has its origin in the development of robotics and advanced technology during the Second World War. The world of games is not so far from the ideals for which humanity is fighting today. A happy society, the supremacy of science, ideal cities with green and sunny parks and squares, the automation of everyday life and the desire to reach the stars. We can get all this in the near future. But should we look at the underside of an ideal world? Could something like this have already happened? And what can it lead to?'),
    ('Dead Space Xbox', '359.99', '78', '2',
    'A DEEPER AND MORE CAPTIVATING EXPERIENCE. The sci-fi survival horror classic Dead Space returns, completely rebuilt from the ground up to offer a deeper and more immersive experience. This remake brings stunning visual fidelity, suspenseful atmospheric sound and gameplay improvements, while staying true to the thrilling vision of the original game. HORROR SCIENCE FICTION THE ULTIMA GENERATION. Isaac Clarke is an ordinary engineer on a mission to repair a vast mining vessel, the USG Ishimura, only to discover that something has gone horribly wrong. The ships crew has been slaughtered, and Isaacs beloved partner, Nicole, is lost somewhere on board.'),
    ('The Legend of Zelda: Breath of the Wild - Nintendo Switch', '299.99', '69', '2',
    'Step into a world of discovery, exploration and adventure in The Legend of Zelda: Breath of the Wild, a game that transcends all boundaries in this highly acclaimed series. Travel across fields, through forests and mountain peaks as you discover what has become of the ruined kingdom of Hyrule in this thrilling adventure. Explore the wilds of Hyrule any way you want. Climb towers and mountain peaks in search of new destinations, then set your own path to get there and jump straight into the wilderness. During your journey you will fight with imposing enemies, hunt wild beasts and collect ingredients for food and elixirs that will help you resist the obstacles that will come your way.'),
    ('Animal Crossing: New Horizons - Nintendo Switch', '239.99', '55', '2',
    'The beloved Animal Crossing franchise is preparing for its debut on Nintendo Switch! If the hustle and bustle of modern life has gotten you down, Tom Nook has a new adventure up his sleeve that he knows youll love: the Nook Inc. Island Escape Package! Sure, youve crossed paths with colorful characters. But deep down, isnt there a part of you that yearns for freedom? Then maybe a long walk on the beach of a deserted island is just what the doctor recommended. Quiet creativity and charm await as you roll up your sleeves and transform your own life into what you want. Gather resources and craft everything from creature comforts to useful tools.'),
    ('Super Mario Odyssey - Nintendo Switch', '234.99', '19', '2',
    'Super Mario Odyssey is the first sandbox game that will allow Mario to explore his own world since Super Mario 64 on the Nintendo 64 and Super Mario Sunshine on the Nintendo GameCube. Mario leaves the Mushroom Kingdom and embarks on a journey with new experiences and mysterious places, such as navigating between worlds via an airship and being able to throw Marios cap.');