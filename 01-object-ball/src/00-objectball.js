const game = gameObject();
const teams = Object.values(game)

function gameObject() {
  return {
    home: {
      teamName: "Brooklyn Nets",
      colors: ["Black", "White"],
      players: {
        "Alan Anderson": {
          number: 0,
          shoe: 16,
          points: 22,
          rebounds: 12,
          assits: 12,
          steals: 3,
          blocks: 1,
          slamDunks: 1,
        },
        "Reggie Evens": {
          number: 30,
          shoe: 14,
          points: 12,
          rebounds: 12,
          assits: 12,
          steals: 12,
          blocks: 12,
          slamDunks: 7,
        },
        "Brook Lopez": {
          number: 11,
          shoe: 17,
          points: 17,
          rebounds: 19,
          assits: 10,
          steals: 3,
          blocks: 1,
          slamDunks: 15,
        },
        "Mason Plumlee": {
          number: 1,
          shoe: 19,
          points: 26,
          rebounds: 12,
          assits: 6,
          steals: 3,
          blocks: 8,
          slamDunks: 5,
        },
        "Jason Terry": {
          number: 31,
          shoe: 15,
          points: 19,
          rebounds: 2,
          assits: 2,
          steals: 4,
          blocks: 11,
          slamDunks: 1,
        },
      },
    },
    away: {
      teamName: "Charlotte Hornets",
      colors: ["Turquoise", "Purple"],
      players: {
        "Jeff Adrien": {
          number: 4,
          shoe: 18,
          points: 10,
          rebounds: 1,
          assits: 1,
          steals: 2,
          blocks: 7,
          slamDunks: 2,
        },
        "Bismack Biyombo": {
          number: 0,
          shoe: 16,
          points: 12,
          rebounds: 4,
          assits: 7,
          steals: 7,
          blocks: 15,
          slamDunks: 10,
        },
        "DeSagna Diop": {
          number: 2,
          shoe: 14,
          points: 24,
          rebounds: 12,
          assits: 12,
          steals: 4,
          blocks: 5,
          slamDunks: 5,
        },
        "Ben Gordon": {
          number: 8,
          shoe: 15,
          points: 33,
          rebounds: 3,
          assits: 2,
          steals: 1,
          blocks: 1,
          slamDunks: 0,
        },
        "Brendan Hayword": {
          number: 33,
          shoe: 15,
          points: 6,
          rebounds: 12,
          assits: 12,
          steals: 22,
          blocks: 5,
          slamDunks: 12,
        },
      },
    },
  };
}

function allPlayersObject() {
  return { ...game.home.players, ...game.away.players };
}

// the logic in this function could have been used inside of numPointsScored()
// and shoeSize(), but whenever you see repeated logic
// you should try to abstract it into a reusable helper function
function playerStats(playerName) {
  const allPlayers = allPlayersObject();
  return allPlayers[playerName];
}

function numPointsScored(playerName) {
    // for (let gameKey in game) {      // nested loops can work, but they 
    
    //   let teamObj = game[gameKey]  // are 'expensive' in terms of how many operations
    //   for (let teamKey in teamObj) {   // are needed to get to the solution
      
      //     let data = teamObj.players
      //     for (let player in data) {
        //       if (player == playerName){
          //         return data[player].points
          //       }
          //     }
          //   }
  // }
  return playerStats(playerName).points;
}

function shoeSize(playerName) {
  return playerStats(playerName).shoe;
}

function findByTeamName(teamName){
    return teams.find((teamObj) => teamObj.teamName === teamName)
}

function teamColors(teamName) {
    return findByTeamName(teamName).colors
}

function playerNumbers(teamName) {
    const playersObj = findByTeamName(teamName).players
    const statsArr = Object.values(playersObj)
    return statsArr.map(statsObj => statsObj.number)
    // return Object.values(findByTeamName(teamName).players).map(statsObj => statsObj.number)
  // this could be a one-line function, but it starts to get difficult to read
}

function teamNames() {
  // return teams.map(function(teamObj){  // syntax with anonymous function
  //   return teamObj.teamName
  // })

  // return teams.map((team) => { return team.teamName}) // syntax with arrow function

  return teams.map(teamObj => teamObj.teamName) // shortest syntax with arrow function
}


function bigShoeRebounds() {
    // get an array of all player stats objects
    let sortedPlayers = Object.values(allPlayersObject())
    // sort the array in place by shoe size
    sortedPlayers.sort((a, b) => {
        return b.shoe - a.shoe
    })
    
    // the statObj with the largest shoe will be the first arr element

    // grab the first element by index and return the rebounds value
    return sortedPlayers[0].rebounds
}

// BONUS

function mostPointsScored(){
    // get a matrix of all players (array of arrays) that will keep the player name associated with their stats, but in a sortable structure
    let sortedPlayers = Object.entries(allPlayersObject())
    sortedPlayers.sort((a,b) => {
      if (a[1].points < b[1].points) return -1;
      if (a[1].points > b[1].points) return 1;
      return 0
    })
    // debugger
    // the sort was ascending order, so we need to use the last index of the array to grab the last element
    // since the last element is also an array, we need another square bracket to get the name instead of the stats object
    return sortedPlayers[sortedPlayers.length - 1][0]
  }
  
  function winningTeam(){
    // I want to create an array of team objs. I want an arr so I can sort it by team scores
    // I'll create my own objects, with just the team name and total score
    // I can use Object.values and reduce()
    // let teamsWithScores = [  // too much hard coding!
    //   {
    //     teamName: game.home.teamName,
    //     score: Object.values(game.home.players).reduce((sum, playerStats) => sum + playerStats.points, 0)
    //   },
    //   {
    //     teamName: game.away.teamName,
    //     score: Object.values(game.away.players).reduce((sum, playerStats) => sum + playerStats.points, 0)
    //   }
    // ]
    let teamsWithScores = teams.map(teamObj => { // ah, better! will work no matter how many teams, and 
      return {                                    // I'm not repeating myself
        teamName: teamObj.teamName,
        score: Object.values(teamObj.players).reduce((sum, playerStats) => sum + playerStats.points, 0)
      }
    })
    // debugger
    // I'll sort my custom array by the score and then take the first element from the array
    const winner = teamsWithScores.sort((a, b) => b.score - a.score)[0]
    return winner.teamName // use .dotnotation to return the name of the winning team
  }
  
  // this question is faulty in that there are two players 
  // with equally long names for the longest criteron
  function playerWithLongestName(){
    // Object.keys returns an array of strings-the player names
    // Then we sort those strings in the array by their length property
    let sortedNames = Object.keys(players).sort((a, b) => b.length - a.length)
    // We can grab the first element from the sorted array with [] index notation
    return sortedNames[0]
  }
  
  // SUPER BONUS
  
  function doesLongNameStealATon(){
    let sortedPlayers = Object.entries(players)
    // console.log('sortedPlayers: ', sortedPlayers);
    sortedPlayers.sort((a, b) => {
      if (a[1].steals < b[1].steals) return -1;
      if (a[1].steals > b[1].steals) return 1;
      return 0
    })
    const mostStealsPlayer = sortedPlayers[0][0]
    return playerWithLongestName() == mostStealsPlayer
  }
  
  // here's one I made up to use .filter()
  // returns an array of the player names who have shoe sizes bigger than 15
  function bigFeetPlayers(){
    // Object.entries keeps player names associated with their stats
    const playerArr = Object.entries(players)
    // debugger
    // .filter will return a new array of player arrays only with shoe > 15, then .map will transform that into an array of just the name strings
    return playerArr.filter(player => player[1].shoe > 15).map(pArr => pArr[0])
  }
  
  
  
  // Object.keys: http://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys
  // Object.values: http://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values
  // Object.entries: http://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries
  // for...in loop: http://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in
  
  console.log('numPointsScored: ', numPointsScored("Brendan Hayword"))
  console.log('shoeSize: ', shoeSize('Ben Gordon'));
  console.log('playerStats: ', playerStats('Jeff Adrien'));
  console.log('findByTeamName: ', findByTeamName('Brooklyn Nets'));
  console.log('teamColors: ', teamColors('Charlotte Hornets'));
  console.log('teamNames: ', teamNames());
  console.log('playerNumbers: ', playerNumbers('Brooklyn Nets'));
  console.log('bigShoeRebounds: ', bigShoeRebounds());
  console.log('mostPointsScored: ', mostPointsScored());
  console.log('winningTeam: ', winningTeam());
  
  // debugger
  