// PROBADO EN NODE 12.22.1
// Para que corra debe tener el ambiente virtual de Python activo

const { spawn, exec } = require('child_process');
let timerArriba = 4000;
let timerAbajo = 1500;

let startProcess = () => {
    const ls = spawn('py -m celery -A flaskr.tareas.tareas worker -l info', [],{ // Este el el comando de consola a ejecutar
        cwd:"./cita", // Aca debe ir el Path desde donde se ejecuta el comando
        shell: true,
        detached: true
    });
    
    ls.on('close', (code) => {
      console.log(`child process exited with code ${code}`);
    });
    
    setTimeout(() => {
        console.log('killing command');
        exec('killall celery'); // Comando para detener procesos en Windows. Para otros OS se debe modificar
    }, timerArriba);

    setTimeout(() => {
        console.log('Starting command');
        startProcess()  
    }, timerArriba + timerAbajo);
}

startProcess();

