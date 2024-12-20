const blackListed = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  if (blackListed.includes(phoneNumber)) {
    console.log(`Phone number ${phoneNumber} is blacklisted`);
    done()
  } else {
    job.progress(0, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    job.progress(50, 100);
    done();
  }
}

const kue = require('kue');

const queue = kue.createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
