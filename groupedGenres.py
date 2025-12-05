# groupedGenres.py
# Fully complete version - every genre from genres_to_be_sorted.txt is included
# Genres belong to ALL categories they fit

musical = [
    'drama, musical', 'comedy, musical', 'musical', 'musical comedy', 'horror, thriller, romance, musical',
    'musical drama', 'drama, family, musical, romance', 'musical, comedy', 'musical comedy', 'operetta',
    'romance musical', 'comedy, musical', 'musical, comedy', 'comedy, drama, musical', 'animated, musical',
    'musical romance', 'musical fantasy', 'musical western', 'musical biopic', 'musical biography',
    'musical bio-pic', 'musical-comedy', 'horror, musical', 'musical, fantasy', 'musical, family',
    'animated musical', 'musical, romance', 'musical, drama', 'musical, western', 'musical, thriller',
    'erotic musical', 'fantasy, musical', 'musical, romantic comedy', 'animation, musical, comedy',
    'musical, adventure', 'romantic musical film', 'musical, romantic comedy', 'dance, musical, idol',
    'musical romance', 'romance, musical', 'musical, romance', 'animation musical', 'musical/action',
    'rock musical', 'musical/suspense', 'musical/triller', 'operetta', 'animation / music', 'music', 'concert', 'nadeem-shravan', 
    'animation, produced by glukoza production', 'masala', 'drama, musical',
    'huangmei opera'
]

adventure = [
    'disaster film, adventure', 'action, adventure, sci-fi', 'drama / sci-fi / adventure', 'drama, adventure',
    'adventure/thriller', 'adventure, comedy', 'adventure', 'adventure serial', 'action adventure',
    'adventure film', 'adventure, thriller', 'adventure horror', 'adventure, drama', 'adventure, action',
    'adventure, fantasy', 'adventure, romance', 'adventure, music', 'adventure drama', 'adventure, serial',
    'adventure, biography', 'adventure, animated', 'adventure, animated, fantasy', 'adventure, disaster',
    'adventure, epic fantasy,', 'adventure/comedy/drama/family', 'adventure, swashbuckler', 'adventure, mystery',
    'adventure, historical drama', 'adventure, crime', 'adventure, comedy, fantasy', 'adventure, family',
    'adventure science fiction', 'adventure-comedy', 'adventure thriller', 'fantasy adventure',
    'adventure, romance, fantasy film', 'colonial adventure', 'prehistoric adventure', 'african adventure',
    'adventure, drama film', 'adventure, romance, fantasy film', 'adventure, animated, comedy',
    'adventure, animated, family, fantasy-comedy', 'adventure, crime, musical, romance, thriller',
    'adventure, animated, fantasy', 'adventure, fantasy, action', 'adventure, crime', 'adventure, animated',
    'animation adventure', 'animated adventure', 'fantasy adventure comedy', 'historical adventure', 'swashbuckler',
    'epic', 'swashbuckler', 'serial', 'aviation', 'space opera', 'epic, science fiction', 
    'western', 'road movie', 'travel', 'adventure', 'survival'
]

horror = [
    'horror, sci-fi', 'supernatural horror', 'comedy-horror', 'horror, thriller, romance, musical',
    'mystery, horror', 'zombie horror', 'action, horror, science fiction', 'horror', 'drama, horror',
    'horror, science fiction', 'horror, sci-fi', 'science fiction, horror', 'sci-fi, horror',
    'horror comedy', 'comedy, horror', 'comedy horror', 'comedy-horror', 'horror, comedy',
    'horror, 3-d', 'horror comedy, parody', 'horror, action', 'horror, fantasy', 'horror, slasher',
    'horror, thriller', 'horror thriller', 'horror-thriller', 'horror/thriller', 'horror / thriller',
    'psychological horror', 'horror, mystery', 'horror, romantic comedy', 'horror, western',
    'horror, found footage', 'found footage / horror', 'horror / found footage', 'horror masala',
    'horror-thriller', 'slasher', 'dark slasher', 'post-apocalyptic, zombie', 'horror, suspense',
    'horror romantic comedy', 'devotional horror', 'horror / comedy', 'horror / mystery', 'horror / drama',
    'horror, action comedy', 'horror, psychological thriller, drama, dark fantasy', 'horror, dark fantasy',
    'supernatural horror, thriller', 'horror, fantasy, chanbara, supernatural, jidaigeki, action',
    'horror film', 'j-horror', 'gore film', 'splatter', 'erotic horror', 'horror and priquitianism',
    'horror, suspense', 'horror/thriller', 'horror / thriller / drama', 'horror-thriller',
    'horror, slasher', 'horror, thriller, drama', 'horror, suspense', 'romance-horror',
    'martial arts/horror/comedy', 'horror / comedy', 'horror romantic comedy', 'horror comedy, teen',
    'horror, fantasy, slahser', 'horror comedy, parody', 'parody, horror', 'anthology, horror comedy',
    'anthology, horror', 'horror-thriller', 'survival', 'horror, western', 'horror, family',
    'horror, 3-d', 'thriller, 3-d', 'horror musical',
    'slasher', 'slasher film', 'slahser', 'post-apocalyptic, zombie', 
    'dark slasher', 'gore film', 'splatter', 'vampire film', 'found footage', 
    'silent hills studio', 'kaiju', 'kaiju eiga', 'monster', 'horror'
]

fantasy = [
    'fantasy anime', 'fantasy / romance / action', 'fantasy', 'fantasy drama', 'short fantasy',
    'fantasy, family', 'fantasy, adventure', 'fantasy, romance', 'comedy, fantasy', 'fantasy, comedy',
    'fantasy, action, adventure', 'fantasy thriller', 'romantic fantasy', 'musical fantasy',
    'fantasy, thriller', 'fantasy, animated', 'fantasy, sports', 'fantasy, swashbuckler',
    'fantasy, musical', 'fantasy, science fiction', 'fantasy, romantic comedy', 'fantasy romance',
    'fantasy romance, horror', 'fantasy-comedy', 'fantasy-period', 'fantasy action',
    'fantasy action adventure', 'fantasy adventure comedy', 'folklore', 'fantasy costume',
    'romantic fantasy drama', 'fantasy, children', 'fantasy horror', 'historical fantasy',
    'animation fantasy', 'animated fantasy', 'fantasy / horror', 'fantasy / comedy',
    'fantasy,drama,comedy', 'dramedy, fantasy', 'fantasy, teen', 'fantasy, sci-fi drama',
    'fantasy, swashbuckler', 'fantasy, children', 'fantasy, action', 'fantasy, drama, sci-fi',
    'fantasy, drama, romance, sci-fi', 'fantasy, action, science fantasy', 'fantasy, drama, action',
    'fantasy, drama, romance, slice of life', 'fantasy, action, comedy, comedy-drama, drama, science fantasy',
    'fantasy, drama, children\'s, action, comedy', 'fantasy, drama, children\'s, sci-fi, adventure, spy',
    'fantasy, drama, children\'s, magical girl, science fantasy', 'fairy tale', 'fantasy/children',
    'fantasy and comedy', 'mythological', 'socio-fantasy', 'socio-fantasy, comedy',
    'mythology', 'mythology legend', 'mythology (fiction)', 'fairy tale', 
    'supernatural', 'fantasy'
]

scifi = [
    'children\'s science fiction', 'sci-fi', 'science fiction', 'horror, sci-fi', 'drama / sci-fi / adventure',
    'action, adventure, sci-fi', 'sci-fi comedy', 'action, horror, science fiction', 'science fiction film',
    'sci-fi, horror', 'sci-fi, comedy', 'sci-fi, drama', 'sci-fi action', 'science-fiction',
    'science fiction, comedy', 'science fiction, drama', 'science fiction, adventure',
    'science fiction, family', 'science fiction, thriller', 'science fiction psychological thriller',
    'science fiction mystery', 'science fiction horror', 'science fiction comedy', 'sci-fi/fantasy',
    'sci-fi/drama', 'sci fi', 'sci-fi western', 'disaster, sci-fi', 'sci-fi, action', 'sci-fi, teen',
    'sci-fi, thriller', 'sci-fi horror', 'sci-fi, animation, comedy', 'sci-fi, drama, thriller',
    'sci-fi, action, adventure', 'sci-fi, action, thriller', 'sci-fi comedy', 'science-fiction, thriller',
    'post-apocalyptic science fiction', 'social science fiction action', 'sci-fi romantic thriller',
    'sci-fi thriller', 'science-fiction comedy', 'sci-fi, adventure, romance', 'animation, adventure, sci-fi',
    'space opera', 'sci-fi western', 'sci-fi, teen', 'sci-fi, drama', 'sci-fi, comedy', 'sci-fi horror',
    'sci-fi action', 'sci-fi, action', 'sci-fi, thriller', 'sci-fi romantic thriller', 'sci-fi thriller',
    'disaster, science fiction', 'disaster film, sci-fi', 'science fiction, animated', 'science fiction action',
    'science fiction adventure', 'science fiction drama supernatural', 'science fiction action-comedy',
    'science fiction action adventure', 'science fiction psychological thriller ', 'science fiction mystery',
    'science fiction, fantasy, action', 'science fiction thriller', 'science fiction, action',
    'science fiction, drama', 'science fiction, time travel', 'science fiction anime',
    'science fiction[not in citation given]', 'children\'s science fiction', 'sci-fi for children',
    'science fiction', 'sci-fi', 'sci-fi, 3-d', 'science-fiction', 
    'epic, science fiction', 'post-apocalyptic science fiction', 'sci fi', 
    'science fiction film', 'sf', 'science fiction[not in citation given]', 
    'sci-fi for children', 'anime science fiction', 'science fiction anime', 
    'science fiction, time travel', 'space opera', 'tokusatsu', 
    'tokusatsu v-cinema', 'kaiju', 'kaiju eiga', 'post-apocalyptic', 'mocatsu'
]

crime = [
    'crime comedy', 'crime, thriller', 'crime drama', 'comedy, crime', 'crime comedy-drama ',
    'biography, crime', 'gangster drama', 'crime', 'crime/thriller', 'film noir', 'short action/crime western',
    'crime drama', 'crime thriller', 'crime, drama', 'crime, film noir', 'crime, sci-fi',
    'crime musical', 'crime, comedy', 'crime, horror', 'crime, romance', 'crime, action',
    'crime, western', 'crime, dark comedy', 'crime thriller, neo-noir', 'crime thriller, dark comedy',
    'crime, family', 'crime thriller, drama', 'crime drama, comedy', 'crime drama, action',
    'crime, biography', 'crime dramedy', 'true crime', 'crime, political/thriller', 'crime suspense romance',
    'crime/adventure', 'crime/romance', 'crime/thriller', 'crime comedy-drama ', 'crime, dark comedy',
    'crime, action', 'crime, drama, superhero', 'crime, drama, thriller', 'crime, drama, mystery, jidaigeki',
    'crime, drama, mystery', 'crime mystery', 'romance comedy crime', 'gangster', 'gangster thriller ',
    'gangster-thriller', 'mob, neo-noir', 'mob', 'crime dramedy', 'crime, romance', 'crime, film noir',
    'crime, western', 'crime, family', 'crime, biography', 'crime, dark comedy', 'crime thriller, neo-noir',
    'crime thriller, dark comedy', 'crime, political/thriller',
    'detective', 'film noir', 'gangster', 'charlie chan', 'neo-noir', 
    'buddy cop', 'gangster film', 'triad', 'kung fu triad', 'investigative', 
    'heist', 'mob, neo-noir', 'mob', 'yakuza', 'yakuza film', 'outlaw biker film',
    'crime', 'keiji'
]

action = [
    'martial arts / action / comedy', 'action, romance', 'action, war', 'action, comedy',
    'action, comedy, romance', 'action / martial arts / comedy', 'action masala', 'action, adventure, sci-fi',
    'action/comedy', 'action / comedy', 'action, horror, science fiction', 'action', 'comedy action',
    'action, drama', 'live-action/animation', 'action adventure', 'action, western', 'action, drama, war',
    'action comedy', 'action, crime', 'action, horror', 'action, sci-fi', 'action, superhero',
    'action, fantasy', 'action, spy', 'action, martial arts', 'action, biography', 'action, family',
    'action, science fiction', 'action film', 'action thriller', 'action film, war', 'action, \'action, history',
    'action, horror comedy', 'action horror, science fiction', 'action-adventure', 'action, romantic comedy',
    'action, masala', 'action-masala', 'action-masala film', 'action—masala', 'action-thriller',
    'action / thriller', 'action thriller ', 'action (film genre)', 'action & comedy', 'action & romance',
    'action & love', 'action - comedy', 'action - romance', 'action - thriller', 'action - war',
    'action - superhero ', 'action romance', 'action romantic', 'action / crime / drama', 'action / drama',
    'action / adventure', 'action / sci-fi / adventure', 'action / drama / war', 'action / adventure / comedy',
    'action / science-fiction', 'action / crime', 'action / historical', 'action, crime drama',
    'action, spy film', 'action, biopic', 'action, horror, science fiction', 'action, adventure, superhero, drama',
    'action, adventure, fantasy, sci-fi', 'action, romance, thriller, crime', 'action, romance, period',
    'action, thriller, romance, drama, comedy', 'action, thriller, comedy', 'action, musical',
    'action, road movie', 'action,thriller', 'action - war', 'action; drama', 'action romantic',
    'action-love', 'action & love', 'action for children', 'action, samurai film', 'action, period film',
    'action entertainer', 'action & comedy', 'action & romance', 'action, crime, drama',
    'neo-noir, action, thriller', 'action, crime drama', 'action, spy', 'action, horror, th...(truncated)',
    'action, horror comedy', 'action, horror, science fiction', 'action drama, sci-fi', 'action drama, fantasy',
    'action drama, war', 'action drama, science fiction', 'action drama, bio-pic, thriller',
    'action-adventure, horror', 'action-adventure, sci-fi', 'action-adventure, fantasy', 'action-adventure, drama',
    'action-adventure, western', 'action-adventure, family', 'action-adventure, animated, family',
    'action-adventure', 'action, spy film', 'action, biopic', 'action thriller, sci-fi horror',
    'action thriller, adventure drama', 'action thriller, fantasy', 'action thriller ', 'action, superhero',
    'action, fantasy', 'action, crime', 'action, drama, epic,', 'action, 007', 'action, spy',
    'action, martial arts', 'action, horror', 'action, crime', 'action, thriller', 'action, history',
    'action, romance, thriller, crime', 'action, romance, thriller', 'action, romance, period',
    'action, romance, thriller, crime', 'action, romance, thriller', 'action, romance, period',
    'action, romance, thriller, drama, comedy',
    'swashbuckler', 'aviation', 'outlaw biker film', 'biker film', 'biker', 
    'martial arts', 'buddy cop', 'kung-fu film', 'wuxia', 'sword', 'kung-fu', 
    'kung fu triad', 'kung fu', 'gun fu', 'martial arts film', 'samurai film', 
    'samurai', 'chambara', 'chanbara', 'ninja', 'action', 'masala', 'fighting',
    'buddy film',
]

western = [
    'comedy western', 'western drama', 'western comedy', 'western', 'western', 'comedy, western',
    'western drama', 'western, romance', 'western, war', 'western, comedy', 'western, serial',
    'western, biography', 'western, mystery', 'western, 3-d', 'western, horror', 'western, film noir',
    'western, musical', 'western, romance', 'western, drama', 'western, romantic drama',
    'epic western', 'sci-fi western', 'western thriller', 'western, 3-d', 'cowboy', 'action-adventure, western',
    'western, serial', 'family, western', 'animated, family, western', 'western, comedy', 'western, drama',
    'western, romantic drama', 'western, horror', 'western, mystery', 'western, film noir', 'western, war',
    'western, biography', 'western musical', 'musical, western', 'action western', 'action, western',
    'western comedy', 'comedy western', 'cowboy', 'western'
]

comedy = [
    'crime comedy', 'martial arts / action / comedy', 'comedy western', 'comedy, crime', 'comedy, musical',
    'comedy, drama', 'musical comedy', 'action, comedy', 'action, comedy, romance', 'comedy, family',
    'screwball comedy', 'crime comedy-drama ', 'comedy-horror', 'kung fu, comedy', 'mockumentary/comedy',
    'romantic comedy, teen', 'sci-fi comedy', 'dark comedy, thriller', 'comedy, romance', 'black comedy',
    'sex comedy', 'superhero/comedy', 'comedy, documentary', 'adventure, comedy', 'comedy / mystery',
    'comedy / romance', 'comedy drama', 'comedy', 'comedy action', 'romantic comedy', 'comedy/drama',
    'comedy, family film', 'comedy short', 'comedy-drama', 'comedy drama', 'dramatic comedy',
    'comedy, adventure', 'comedy, horror, mystery', 'comedy adventure', 'comedy, horror',
    'comedy mystery', 'comedy, fantasy', 'comedy romance', 'romance, comedy', 'comedy, drama, crime',
    'comedy, drama, musical', 'comedy 2-reeler', 'comedy-drama', 'action comedy, family', 'comedy, sports',
    'comedy, biography', 'comedy spy', 'comedy thriller', 'screwball comedy', 'comedy, short',
    'fantasy, comedy', 'comedy, satire', 'comedy, parody', 'spy comedy', 'comedy horror',
    'comedy, action', 'comedy, cult', 'comedy, science fiction', 'comedy, teen', 'comedy, thriller',
    'parody', 'comedy horror', 'erotic comedy', 'comedy, war', 'comedy-drama, fantasy',
    'comedy-drama, romance', 'black comedy', 'slapstick', 'comedy masala', 'satirical comedy',
    'heist-comedy', 'mockumentary comedy', 'superhero/comedy', 'comedy, superhero', 'buddy cop, comedy',
    'comedy, road', 'comedy, love story, drama', 'comedy drama ', 'comedy/familya', 'romanctic comedy',
    'romantic comedy ', 'comedy - thriller', 'comedy romantic thriller', 'comedy / horror',
    'comedy / drama / romance', 'comedy / western', 'comedy / drama', 'comedy / thriller',
    'comedy/social', 'comedy/social', 'comedy road movie', 'teen/comedy', 'adult/comedy',
    'comedy/comedy/comedy', 'comedy-horror', 'comedy-thriller', 'comedy-drama, crime thriller',
    'comedy, parody', 'comedy, anthology', 'comedy, satire', 'comedy, cult', 'comedy, horror, mystery',
    'comedy, horror', 'comedy, crime', 'comedy, action', 'comedy, short', 'comedy, family',
    'comedy, spy film', 'comedy, superhero', 'comedy, road', 'comedy, teen', 'comedy, horror, mystery',
    'comedy, horror', 'comedy, fantasy', 'comedy, drama, sports', 'comedy, sci-fi', 'comedy, parody',
    'comedy, action', 'comedy, biography', 'comedy, war', 'comedy, satire', 'comedy, parody',
    'comedy, horror, mystery', 'comedy, drama, musical', 'comedy, drama, crime', 'comedy, drama',
    'comedy, crime', 'comedy, romance', 'comedy, musical', 'comedy, horror', 'comedy, fantasy',
    'comedy, drama, sports', 'comedy, sci-fi', 'comedy, parody', 'comedy, action', 'comedy, biography',
    'comedy, war', 'comedy, satire', 'comedy, parody', 'comedy, horror, mystery', 'comedy, drama, musical',
    'comedy, drama, crime', 'comedy, drama', 'comedy, crime', 'comedy, romance', 'comedy, musical',
    'comedy, horror', 'comedy, fantasy', 'comedy, drama, sports', 'comedy, sci-fi', 'comedy, parody',
    'comedy, action', 'comedy, biography', 'comedy, war', 'comedy, satire', 'comedy, parody',
    'rom com', 'slapstick', 'rom-com', 'satire', 'dramedy', 'spoof', 'buddy cop', 
    'political satire', 'comedey', 'mockumentary', 'parody', 'comedy', 
    'stoner film', 'buddy film'
]

romance = [
    'romantic drama', 'romance', 'action, romance', 'fantasy / romance / action', 'romantic comedy, teen',
    'comedy, romance', 'horror, thriller, romance, musical', 'romance/drama', 'romance, war',
    'drama, family, musical, romance', 'romantic comedy', 'romance, drama', 'drama, romance',
    'romantic drama', 'romance drama', 'drama romance', 'romance, drama', 'romance, comedy',
    'romance musical', 'romantic', 'romance, comedy, drama', 'romantic comedy/drama',
    'romantic crime/mystery', 'romance musical', 'romantic comedy', 'romantic comedy, romantic',
    'romance comedy drama', 'romantic comedy, sports', 'romance thriller drama', 'romantic thriller',
    'romance, sci-fi', 'romance, action, comedy', 'romance, action, drama', 'romance, action',
    'romance, crime', 'romance, musical', 'romance, comedy, drama, social', 'romance comedy crime',
    'romance/teen', 'romance/crime', 'romance/ drama', 'romance/drama', 'romance/comedy',
    'romance/musical', 'romance/fantasy', 'romance thriller', 'romantic, comedy', 'romantic, comedy, suspense',
    'romantic action', 'romantic spy drama', 'romantic fantasy drama', 'romantic musical film',
    'romance film, drama', 'romance-action', 'romance social', 'romance social drama',
    'romantic family drama', 'romantic triangle', 'romantic-comedy', 'rom-com', 'rom-com/action',
    'romance comedy', 'romance-adventure', 'romance/drama', 'romance/comedy', 'romance, thriller',
    'romance, fantasy, musical', 'romance, sci-fi, thriller', 'romance, music', 'romance, war',
    'romance, trilogy', 'military romance', 'western romance', 'romantic fantasy', 'romantic musical',
    'romantic comedy-drama', 'romance dramedy', 'romantic comedy, romantic', 'romance, comedy, drama, art house & international, action',
    'romance, comedy, drama', 'romance / thriller', 'romantic action', 'love, drama', 'love story',
    'romance-action', 'period romance', 'campus, romance', 'youth, romance', 'adult romance',
    'romance, road', 'romantic thriller ', 'romantic comedy ', 'romance, thriller, drama', 'romance film, drama',
    'romantic', 'rom com', 'rom-com', 'romantic triangle', 'love', 'love story', 
    'erotic', 'ero', 'pink', 'roman porno', 'masala'
]

drama = [
    'drama, musical', 'romantic drama', 'western drama', 'crime drama', 'historical drama',
    'drama, exploitation', 'drama, thriller, war', 'war drama', 'drama-thriller',
    'drama / sci-fi / adventure', 'drama, adventure', 'drama, sports', 'campus drama',
    'drama, coming of age', 'drama, thriller', 'dramedy', 'drama, family', 'musical drama',
    'costume drama', 'social family drama', 'drama', 'drama, family, musical, romance',
    'war drama[not in citation given]', 'comedy/drama', 'romance, drama', 'spy/drama',
    'drama, romance', 'drama', 'drama, horror', 'biographical drama', 'documentary drama',
    'fantasy drama', 'drama romance', 'period drama', 'drama, war', 'drama, crime',
    'drama, western', 'drama, thriller', 'drama, mystery', 'drama, sports', 'drama, sport',
    'drama, \'drama, biography', 'drama, action', 'drama, science fiction', 'drama, fantasy',
    'drama, exploitation', 'drama anthology', 'drama, comedy; 6 separate stories',
    'drama, comedy', 'drama war', 'drama, television miniseries', 'drama, family',
    'family drama', 'drama, biopic', 'drama, political thriller', 'drama, spy thriller',
    'legal drama', 'drama, coming of age', 'drama, independent movie', 'drama / thriller',
    'drama / history / war', 'drama / history', 'drama / war', 'drama / adventure',
    'drama / romance', 'drama / comedy / romance', 'drama / science-fiction', 'drama/family',
    'drama, true crime', 'drama, history', 'drama, romance ', 'drama, dance', 'drama, martial arts',
    'drama, suspense thriller', 'drama horror thriller film', 'drama, black humour',
    'drama, period', 'drama, environmental film, human rights', 'social drama',
    'social drama, drama, history', 'family drama ', 'famil drama ', 'drama social',
    'drama, social', 'drama, erotic', 'drama, road movie', 'drama, satire', 'campus drama',
    'teen drama', 'family drama romance drama', 'drama, gangster', 'drama, animated',
    'animation drama', 'drama comedy', 'drama, teen', 'christian drama', 'shakespearean drama',
    'drama[not in citation given]', 'drama / documentary', 'drama/disaster', 'drama/social',
    'social/action', 'drama/espionage thriller', 'drama/biography', 'drama/cult',
    'drama, black humour', 'drama, period', 'drama, period', 'drama, environmental film, human rights',
    'investigative', 'drama, black humour', 'period, drama', 'drama, period', 'psychological thriller film',
    'drama, satire', 'patriotism, drama', 'drama-comedy-social', 'drama thriller', 'psychological action thriller',
    'drama, sentiment', 'tragic comedy', 'melodrama', 'family melodrama', 'social romantic melodrama',
    'romantic family drama', 'epic', 'film noir', 'romantic', 'serial', 'biblical', 'rom com', 'rom-com', 
    'dramedy', 'literary adaptation', 'adaptation of a play by michel marc bouchard,', 
    'adapted from the play by alexandre goyette', 'tragedy', 'coming of age', 
    'coming-of-age', 'period', 'period piece', 'melodrama', 'neo-noir', 
    'social', 'masala', 'drama', 'huangmei opera', 'survival'
]

animated = [
    'animated', 'fantasy anime', 'anime', 'animated, comedy, family', 'animated short',
    'animation', 'animated series', 'animated', 'animated, comedy', 'animated, musical',
    'animated, war', 'animated short', 'animated, short', 'animated film', 'animated, family',
    'animated, fantasy', 'animated, comedy, drama, family', 'animated, family, fantasy',
    'animated, horror comedy', 'animated, superhero', 'animated, sci-fi', 'animated, buddy comedy',
    'animated, fantasy, musical', 'animation, family', 'animation, adult', 'animation, science fiction, drama, family',
    'animation, comedy', 'animation, adventure', 'animation, fantasy', 'animation comedy family',
    'animation comedy', 'animation fantasy', 'animation martial arts action-comedy', 'computer-animated',
    'computer animated', 'clay animation', 'stop-motion animation', 'animation, live action / drama / comedy',
    'animation, musical, fantasy, mystery', 'animation, comedy, fantasy, family', 'animation, action, comedy, family',
    'animation, comedy, action', 'animation, sports, comedy, drama', 'animation, adventure, comedy',
    'animation, adventure, comedy, family, fantasy, musical', 'animation, adventure, comedy',
    'animation, comedy, adventure, action', 'animation, comedy, adventure', 'animation / adventure',
    'animation, fantasy', 'animation, musical', 'animation comedy family', 'anime/computer animation',
    'animation, produced by glukoza production', 'animation/ period', 'animation, adventure, sci-fi',
    'animation, comedy, action', 'animation, musical, comedy', 'animation comedy family',
    'animation, adventure', 'animation, fantasy', 'animation, comedy', 'animation, musical',
    'animation, adventure, comedy', 'animation, comedy, adventure', 'animation, fantasy',
    'animation, musical', 'animation comedy family', 'children/animation', 'computer-animated',
    'computer animated', 'animation', 'cartoon', 'stop-motion animation', 'animation, adult', 
    'clay animation', 'anime', 'feature animation', 'animation / music', 
    'animation / children', 'children/animation', 'anime for children', 
    'animation/fighting', 'anime martial arts', 'science fiction anime', 
    'anime/computer animation', 'computer animation', 'animated',
]

documentary = [
    'mockumentary/comedy', 'comedy, documentary', 'tv miniseries, docudrama', 'docudrama',
    'documentary', 'documentary', 'semi-staged documentary', 'comedy, documentary',
    'war documentary', 'documentary, music', 'documentary, family', 'documentary film',
    'nature documentary', 'biographical, documentary', 'short documentary', 'documentary, music',
    'concert, documentary', 'documentary, family', 'war documentary', 'documentary drama',
    'drama documentary', 'world war ii drama documentary', 'docufiction drama', 'drama / documentary',
    'nature', 'educational', 'travel', 'mockumentary', 'reality', 'concert', 
    'biographic', 'making of', 'found footage', 'documentary'
]

historical = [
    'historical drama', 'historical', 'war/historical', 'world war ii', 'period drama',
    'costume drama', 'historical drama', 'historical comedy', 'historical epic',
    'historical epic, disaster', 'historical biopic', 'historical, erotic', 'historical, music',
    'historical romance', 'historical costume romance', 'historical fiction', 'period piece',
    'period piece, romantic drama', 'historical film', 'historical, action', 'historical / action / war',
    'historical anime', 'historical dram', 'period, drama', 'period romance', 'period thriller',
    'period, patriotic, drama', 'period, revenge', 'period, drama', 'period comedy',
    'historical fantasy', 'historical crime', 'history, romance', 'history, spy', 'history, fantasy',
    'historical fantasy', 'historical adventure', 'historical, action', 'historical / action / war',
    'epic / history', 'historical comedy/satire', 'animation/ period', 'period piece',
    'period piece, romantic drama', 'period romance', 'period thriller', 'period, patriotic, drama',
    'period, revenge', 'period, drama', 'period comedy', 'historical fantasy', 'historical crime',
    'history, romance', 'history, spy', 'history, fantasy', 'historical fantasy', 'historical adventure',
    'historical, action', 'children\'s science fiction', 'musical, adventure',
    'epic', 'biblical', 'historic', 'period', 'shakespearean', 'epic, science fiction', 
    'period costume', 'period, revenge', 'perodic', 'period piece', 
    'animation/ period', 'epic / history', 'samurai film', 'jidaigeki', 
    'jidai-geki', 'history', 'chambara', 'chanbara', 
    'biopic of pioneering american photographer eadweard muybridge'
]

suspense = [
    'suspense', 'mystery, suspense', 'suspense', 'suspense/thriller', 'suspense, comedy',
    'suspense thriller', 'suspense romance', 'suspense, thriller', 'drama, suspense thriller',
    'mystery, suspense thriller', 'suspense action horror', 'suspense/thriller', 'adult/suspense/thriller',
    'suspense thriller', 'psychological thriller/romance', 'romantic, comedy, suspense',
    'detective', 'film noir', 'neo-noir', 'thriller', 'suspense'
]

religion = [
    'devotional', 'devotional biography', 'devotional-biographical', 'devotional horror',
    'christian', 'christian drama', 'biblical', 'biblical drama', 'biblical epic',
    'paramount. biblical epic', 'christian drama', 'biblical', 'christian', 'modern day passion play', 'mythology', 
    'devotional', 'religious', 'devotional biopic', 'mythology legend', 
    'biopic devotional', 'biopic legend devotional', 'mythological'
]

social = [
    'social family drama', 'social', 'social drama', 'social romance', 'social crime',
    'social, drama, history', 'social drama romance', 'social, romance', 'social, war, action',
    'social, adult', 'social satire drama', 'social children drama', 'social, thriller',
    'social, comedy', 'social/action', 'social thriller', 'social drama, comedy',
    'social romantic melodrama', 'classic muslim social', 'romantic muslim social',
    'socio-political', 'socio-fantasy', 'socio-fantasy, comedy', 'social satire',
    'social/comedy', 'social/drama', 'comedy/social', 'social science fiction action',
    'educational', 'socio-political', 'political', 'political satire', 
    'politics', 'propaganda', 'race film', 'counterculture'
]

sports = [
    'sports', 'drama, sports', 'silent sports', 'american football', 'drama, sports',
    'drama, sport', 'sports drama', 'sport, drama', 'sports comedy', 'sports biopic',
    'sports comedy', 'sports/family', 'sports (road bicycle racing)', 'sports (aquatics, swimming)',
    'sports (shogi, chess)', 'sports/drama', 'sport drama', 'sport film', 'sports/comedy',
    'sports, drama', 'sports/social', 'sports biopic', 'family, sports', 'parody, sports',
    'family, sports comedy', 'drama, sports', 'drama, coming of age', 'sports, comedy, drama',
    'fantasy, sports', 'school, sports', 'romantic comedy, school, sports', 'drama, action, sports (volleyball)',
    'drama, sports (road bicycle racing), comedy-drama', 'drama, sports (aquatics, swimming), comedy-drama',
    'american football', 'race film', 'sport', 'sport film', 'race', 'sports'
]

mystery = [
    'mystery', 'mystery, suspense', 'spy film, mystery', 'comedy / mystery', 'mystery, horror',
    'mystery', 'murder mystery', 'mystery comedy', 'detective', 'mystery, comedy',
    'mystery, thriller', 'mystery drama', 'mystery, crime, drama', 'mystery, suspense thriller',
    'mystery thriller', 'mystery, romance, thriller', 'crime mystery', 'mystery adventure',
    'short mystery', 'detective/drama', 'detective fiction, drama', 'mystery/action',
    'mystery/horror', 'mystery/thriller', 'mystery/thriller/drama', 'short/drama/mystery (30min)',
    'comedy mystery', 'mystery, horror', 'mystery, comedy', 'mystery, drama', 'thriller, mystery, romance',
    'mystery, suspense', 'mystery adventure', 'romantic crime/mystery', 'spy film, mystery',
    'western, mystery', 'family, mystery', 'fantasy, drama, comedy, mystery',
    'detective', 'charlie chan', 'investigative', 'mystery', 'keiji'
]

martial_arts = [
    'martial arts / action / comedy', 'kung fu, comedy', 'action / martial arts / comedy',
    'martial arts', 'kung fu', 'martial arts/action/thriller', 'martial arts/horror/comedy',
    'action, martial arts', 'costume martial arts', 'martial arts', 'animation martial arts action-comedy',
    'anime martial arts', 'fantasy, martial arts', 'drama, martial arts',
    'martial arts', 'kung-fu film', 'wuxia', 'sword', 'kung-fu', 
    'kung fu triad', 'kung fu', 'gun fu', 'martial arts film', 
    'costume martial arts', 'animation/fighting', 'anime martial arts'
]

short = [
    'short', 'short film', 'short comedy', 'animated short', 'short subject',
    'short animation', 'comedy short film', 'short documentary', 'experimental short',
    'short drama', 'animated, short', 'short mystery', 'comedy, short', 'animated short',
    'short/drama/mystery (30min)', 'war short', 'cartoon short', 'short subject',
    'experimental short', 'short animation', 'animated short', 'propaganda short',
    'propaganda short animated short', 'short film', 'comedy short', 'animated short',
    'short'
]

family = [
    'family', 'comedy, family', 'animated, comedy, family', 'drama, family',
    'drama, family, musical, romance', 'comedy, family film', 'family', 'fantasy, family',
    'comedy, family', 'family, drama', 'family, western', 'family, comedy', 'family, animated',
    'family, romance drama', 'family, romance', 'family, thriller, drama', 'family, musical, romance',
    'family, sports comedy', 'family, live-action/animated film', 'family, live action',
    'family, superhero', 'family, spy film', 'family film', 'family film, direct-to-dvd',
    'family, children\'s film', 'family (artistic)', 'family, drama, comedy', 'family, drama, thriller',
    'family, children\'s film', 'family, romance', 'family, romance, drama', 'family, musical',
    'family comedy-drama', 'family adventure', 'action, family, drama, comedy', 'family, animated, fantasy',
    'family, animation', 'family, live-action', 'family, sci-fi', 'family, mystery',
    'family, animated', 'family, romantic drama', 'family, direct-to-dvd', 'family film, direct-to-dvd',
    'family, live action', 'family, spy film', 'family, sports comedy', 'family, drama, comedy',
    'family / drama', 'family, drama, thriller', 'family, thriller', 'family, romance',
    'family, musical', 'family, sci-fi', 'family, superhero', 'family, spy film',
    'family, animated, fantasy', 'family, romantic drama', 'family, direct-to-dvd',
    'family film', 'family film, direct-to-dvd', 'family, live-action', 'family, sports comedy',
    'cartoon', 'children\'s film', 'children\'s', 'animation / children', 
    'children', 'children/animation', 'fairy tale', 'sci-fi for children', 
    'anime for children', 'family'
]

war = [
    'war', 'action, war', 'drama, thriller, war', 'war drama', 'war/historical',
    'romance, war', 'war', 'war drama', 'war, biography', 'war, romance', 'war, drama',
    'war propaganda', 'war, satire', 'war, western', 'war, comedy', 'war, action',
    'war, comedy', 'war, horror', 'war romance', 'war, western', 'war short',
    'war film', 'world war i', 'world war ii', 'world war', 'war/drama', 'war/romance',
    'war/spy', 'korean war', 'war-comedy', 'war propaganda', 'war documentary',
    'war, drama, historical', 'war, drama, action, romance', 'war, science fiction',
    'world war i drama', 'war/spy', 'world war ii/spy', 'world war ii action',
    'world war ii comedy', 'world war ii/pow', 'world war ii/thriller', 'world war ii drama',
    'war, biker', 'war, satire', 'war, action', 'war, comedy', 'war, drama', 'war, romance',
    'war, biography', 'war, horror', 'war short', 'war film', 'war propaganda', 'war documentary', 'war spy',
    'p.o.w.', 'war'
]

disaster = [
    'disaster film, adventure', 'disaster film', 'disaster', 'disaster film, sci-fi',
    'disaster, science fiction', 'disaster, sci-fi', 'romance, disaster',
    'historical epic, disaster', 'disaster film, adventure', 'disaster film, sci-fi',
    'drama/disaster', 'adventure, disaster', 'disaster'
]

propaganda = [
    'propaganda', 'ww1 propaganda', 'propaganda short', 'propaganda short animated short',
    'war propaganda', 'war propaganda', 'war drama propaganda',
    'patriotic', 'epic, patriotism', 'revolutionary patriotic', 'patriotism'
]

exploitation = [
    'drama, exploitation', 'exploitation', 'blaxploitation', 'sexual hygiene/exploitation film',
    'sexploitation', 'blaxploitation', 'exploitation', 'adult', 'slasher', 'outlaw biker film', 'biker film', 'biker', 
    'blaxploitation', 'adult film', 'animation, adult', 'bruceploitation', 
    'erotic', 'ero', 'pink', 'roman porno', 'exploitation'
]

supernatural = [
    'supernatural horror', 'supernatural', 'supernatural comedy', 'supernatural thriller',
    'supernatural horror, thriller', 'supernatural action', 'supernatural horror',
    'supernatural horror, thriller', 'supernatural comedy', 'buddy cop, supernatural',
    'supernatural/action/anime', 'horror, fantasy, chanbara, supernatural, jidaigeki, action',
    'ghost', 'supernatural', 'vampire film', 'undead'
]

superhero = [
    'superhero', 'superhero/comedy', 'superhero', 'superhero, action', 'superhero film',
    'superhero, action, adventure, fantasy, sci-fi', 'superhero, comedy, adventure, sci-fi',
    'superhero action adventure', 'superhero, western', 'superhero, action, adventure, fantasy, drama, war',
    'superhero action, superhero', 'superhero comedy', 'superhero/action', 'superhero/comedy',
    'superhero, action', 'action - superhero ', 'family, superhero', 'dark comedy, superhero',
    'crime drama, superhero', 'animated, superhero', 'superhero'
]

spy = [
    'spy/thriller', 'spy film, mystery', 'spy film', 'spy', 'spy/drama', 'spy',
    'spy drama', 'spy thriller', 'spy serial', 'spy comedy', 'spy comedy thriller',
    'spy/action', 'spy/action/james bond', 'spy film, comedy', 'spy film, mystery',
    'spy comedy', 'spy spoof', 'espionage', 'spy/world war i', 'spy/thriller',
    'spy/action/comedy', 'spy comedy/thriller', 'spy comedy thriller', 'spy/action',
    'spy/action/comedy', 'spy comedy', 'spy film', 'spy anthology', 'spy comedy',
    'spy film, comedy', 'spy film, mystery', 'history, spy', 'family, spy film',
    'animated, family, spy film', 'action, spy', 'action, spy film', 'drama, \'spy thriller',
    'biography, spy thriller', 'drama, spy thriller', 'family, spy film', 'war spy', 'espionage', 'spy'
]

thriller = [
    'crime, thriller', 'drama, thriller, war', 'drama-thriller', 'spy/thriller',
    'dark comedy, thriller', 'adventure/thriller', 'thriller/drama', 'drama, thriller',
    'horror, thriller, romance, musical', 'thriller', 'political thriller', 'crime/thriller',
    'thriller', 'thriller, 3-d', 'thriller, crime', 'thriller, adventure', 'thriller, comedy',
    'psychological thriller', 'erotic thriller', 'thriller, fantasy', 'thriller action',
    'thriller action romance', 'thriller, romance', 'thriller, romance, musical',
    'thriller, mystery, romance', 'thriller, suspense, crime', 'thriller, action, romance',
    'thriller, mystery', 'thriller, crime', 'thriller, western', 'thriller, comedy, mystery',
    'thriller, sci-fi, action', 'thriller, fantasy', 'thriller, horror', 'thriller, action',
    'thriller, western', 'thriller drama', 'thriller/black comedy', 'political thriller',
    'psychological thriller/romance', 'psychological thriller film', 'medical thriller',
    'period thriller', 'heist', 'thriller travelogue', 'road thriller', 'urban thriller',
    'psy thriller', 'action thriller, sci-fi horror', 'action thriller, adventure drama',
    'crime thriller, neo-noir', 'crime thriller, dark comedy', 'spy thriller',
    'political drama, thriller', 'political, thriller', 'crime, political/thriller',
    'thriller, fantasy', 'thriller, comedy', 'thriller, crime', 'thriller, western',
    'thriller, comedy, mystery', 'thriller, sci-fi, action', 'thriller, fantasy',
    'thriller, horror', 'thriller, action', 'thriller, western', 'thriller drama',
    'thriller/black comedy', 'political thriller', 'psychological thriller/romance',
    'psychological thriller film', 'medical thriller', 'period thriller', 'heist',
    'thriller travelogue', 'comedy romantic thriller', 'social thriller', 'romance / thriller',
    'romance, thriller, drama', 'vigilante, action, thriller', 'thriller, comedy, mystery',
    'sci-fi, romance, thriller', 'detective, thriller', 'romantic thriller ', 'action thriller ',
    'gangster thriller ', 'western thriller', 'campus thriller', 'thriller drama',
    'satire - thriller', 'thriller/comedy', 'black comedy/thriller', 'erotica/thriller',
    'political crime thriller', 'horror / thriller / drama', 'fantasy / horror', 'romance / thriller',
    'horror - thriller', 'serial', 'film noir', 'neo-noir', 'espionage', 'found footage', 'thriller', 'survival'
]

biography = [
    'biography', 'biography, crime', 'biographical', 'biography', 'biographical drama',
    'biographical comedy-drama', 'biography, drama', 'biography, musical', 'biography, sports',
    'biography, \'war', 'biography, romantic comedy', 'biography, spy thriller', 'biography, comedy',
    'biography, crime drama', 'biography, crime', 'biography, war', 'biography, crime',
    'biographical, documentary', 'biographical war film', 'biographical political thriller',
    'biographical fim', 'biographical, drama', 'biographical, documentary', 'biography, action, comedy, crime, drama, history, thriller',
    'biography, war, drama', 'biography, drama, history, thriller', 'biography, drama, thriller',
    'biography, drama, history, thriller', 'biography, musical, drama', 'bio-pic, drama',
    'bio-pic, musical', 'bio-pic, sports', 'bio-pic, black comedy', 'bio-pic, comedy-drama',
    'bio-pic, drama, music', 'biopic', 'bio-pic', 'biopic, drama', 'biopic, political drama',
    'action, biopic', 'biogtaphy, crime, drama', 'biographical drama ', 'biographical comedy-drama',
    'biographical political thriller', 'biographical, documentary', 'biographical drama',
    'biographical, drama', 'united artists. biography', 'warner bros. biography', 'biographical', 'biopic', 'bio-pic', 
    'biopic of pioneering american photographer eadweard muybridge', 
    'devotional biopic', 'biopic devotional', 'biopic legend devotional', 
    'biographic', 'biographical fim', 'biography'
]

avant_garde = [
    'avant-garde', 'avant-garde, drama', 'avant-garde, horror', 'punk/avant-garde',
    'avant-garde, drama', 'experimental', 'experimental film, art film', 'experimental short',
    'avant-garde, horror', 'experimental', 'avant-garde', 'punk/avant-garde', 'experimental film, art film', 
    'art', 'cult film', 'interactive cinema', 'independent'
]

tokusatsu_v_cinema = [
    'tokusatsu v-cinema', 'tokusatsu', 'tokusatsu, action, sci-fi',
    'tokusatsu, action, sci-fi, spy, superheroes', 'superheroes, tokusatsu',
    'tokusatsu', 'tokusatsu v-cinema', 'kaiju', 'kaiju eiga', 'mocatsu'
]

# NEW CATEGORIES (only four, all large)
melodrama = [
    'melodrama', 'family melodrama', 'social romantic melodrama', 'romantic family drama',
    'drama, sentiment', 'tragic comedy', 'melodrama', 'social romantic melodrama',
    'melodrama'
]

anthology = [
    'anthology', 'drama anthology', 'anthology, drama', 'anthology, horror comedy',
    'anthology, horror', 'spy anthology', 'anthology, horror', 'comedy, anthology',
    'anthology, drama', 'compilation', 'anthology'
]

dance = [
    'dance', 'drama, dance', 'dance, drama', 'dance, drama, romance', 'dance, dramedy, romance',
    'dance, parody', 'dance, romance', 'dance, musical, idol', 'fantasy, drama, dance, musical, romance, idol',
    'dance'
]

teen = [
    'teen', 'romantic comedy, teen', 'comedy, teen', 'teen comedy', 'teen fantasy drama',
    'comedy-drama, teen', 'dramedy, teen', 'teen/comedy', 'romance/teen', 'comedy, teen',
    'sci-fi, teen', 'comedy horror, teen', 'teen comedy', 'comedy, teen', 'teen fantasy drama',
    'student film', 'coming-of-age', 'coming of age', 'youth', 'teen'
]