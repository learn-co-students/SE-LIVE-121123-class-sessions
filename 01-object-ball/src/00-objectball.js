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

function findByTeamname(teamName){
    return teams.find((teamObj) => teamObj.teamName === teamName)
}

function teamColors(teamName) {
    return findByTeamname(teamName).colors
}

function playerNumbers(teamName) {
    const playersObj = findByTeamname(teamName).players
    const statsArr = Object.values(playersObj)
    return statsArr.map(statsObj => statsObj.number)
}

function teamNames() {
    return teams.map(function(teamObj){
        return teamObj.teamName
    })
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

playerStats("Brendan Hayword");
console.log(
  "🚀 ~ file: 00-objectball.js:157 ~ playerStats():",
  playerStats("Brendan Hayword")
);
