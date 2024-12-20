// function

const kue = require('kue');

const queue = kue.createQueue();

const createPushNotificationJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  jobs.forEach(element => {
    const job = queue.create('push_notification_code_3', element).save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', () => {
      console.log(`Notification job ${job.id} failed`);
    });
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationJobs;
