/********************************************************************************
** Form generated from reading UI file 'ConfigureRepos.ui'
**
** Created by: Qt User Interface Compiler version 5.12.9
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef CONFIGUREREPOS_H
#define CONFIGUREREPOS_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QGridLayout *gridLayout;
    QDialogButtonBox *buttonBox;
    QCheckBox *winCheckBox;
    QCheckBox *bsdCheckBox;
    QCheckBox *oracleCheckBox;
    QCheckBox *macosCheckBox;
    QCheckBox *centosCheckBox;
    QCheckBox *debianCheckBox;
    QCheckBox *fedoraCheckBox;
    QPushButton *downloadReposButton;
    QLabel *label;
    QCheckBox *ubuntuCheckBox;
    QPushButton *prepareIsoButton;
    QPushButton *gitResetHardButton;
    QPushButton *gitPullButton;
    QLabel *label_2;
    QLineEdit *leReposPath;
    QPushButton *proxyButton;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(380, 270);
        gridLayout = new QGridLayout(Dialog);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        buttonBox = new QDialogButtonBox(Dialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        gridLayout->addWidget(buttonBox, 8, 0, 1, 3);

        winCheckBox = new QCheckBox(Dialog);
        winCheckBox->setObjectName(QString::fromUtf8("winCheckBox"));

        gridLayout->addWidget(winCheckBox, 5, 1, 1, 1);

        bsdCheckBox = new QCheckBox(Dialog);
        bsdCheckBox->setObjectName(QString::fromUtf8("bsdCheckBox"));

        gridLayout->addWidget(bsdCheckBox, 4, 0, 1, 1);

        oracleCheckBox = new QCheckBox(Dialog);
        oracleCheckBox->setObjectName(QString::fromUtf8("oracleCheckBox"));

        gridLayout->addWidget(oracleCheckBox, 4, 1, 1, 1);

        macosCheckBox = new QCheckBox(Dialog);
        macosCheckBox->setObjectName(QString::fromUtf8("macosCheckBox"));

        gridLayout->addWidget(macosCheckBox, 5, 0, 1, 1);

        centosCheckBox = new QCheckBox(Dialog);
        centosCheckBox->setObjectName(QString::fromUtf8("centosCheckBox"));

        gridLayout->addWidget(centosCheckBox, 3, 1, 1, 1);

        debianCheckBox = new QCheckBox(Dialog);
        debianCheckBox->setObjectName(QString::fromUtf8("debianCheckBox"));

        gridLayout->addWidget(debianCheckBox, 1, 0, 1, 1);

        fedoraCheckBox = new QCheckBox(Dialog);
        fedoraCheckBox->setObjectName(QString::fromUtf8("fedoraCheckBox"));

        gridLayout->addWidget(fedoraCheckBox, 1, 1, 1, 1);

        downloadReposButton = new QPushButton(Dialog);
        downloadReposButton->setObjectName(QString::fromUtf8("downloadReposButton"));

        gridLayout->addWidget(downloadReposButton, 1, 2, 1, 1);

        label = new QLabel(Dialog);
        label->setObjectName(QString::fromUtf8("label"));
        QFont font;
        font.setPointSize(24);
        label->setFont(font);

        gridLayout->addWidget(label, 0, 0, 1, 2);

        ubuntuCheckBox = new QCheckBox(Dialog);
        ubuntuCheckBox->setObjectName(QString::fromUtf8("ubuntuCheckBox"));

        gridLayout->addWidget(ubuntuCheckBox, 3, 0, 1, 1);

        prepareIsoButton = new QPushButton(Dialog);
        prepareIsoButton->setObjectName(QString::fromUtf8("prepareIsoButton"));

        gridLayout->addWidget(prepareIsoButton, 3, 2, 1, 1);

        gitResetHardButton = new QPushButton(Dialog);
        gitResetHardButton->setObjectName(QString::fromUtf8("gitResetHardButton"));

        gridLayout->addWidget(gitResetHardButton, 4, 2, 1, 1);

        gitPullButton = new QPushButton(Dialog);
        gitPullButton->setObjectName(QString::fromUtf8("gitPullButton"));

        gridLayout->addWidget(gitPullButton, 5, 2, 1, 1);

        label_2 = new QLabel(Dialog);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 6, 0, 1, 1);

        leReposPath = new QLineEdit(Dialog);
        leReposPath->setObjectName(QString::fromUtf8("leReposPath"));

        gridLayout->addWidget(leReposPath, 6, 1, 1, 2);

        proxyButton = new QPushButton(Dialog);
        proxyButton->setObjectName(QString::fromUtf8("proxyButton"));

        gridLayout->addWidget(proxyButton, 0, 2, 1, 1);


        retranslateUi(Dialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), Dialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Dialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", nullptr));
        winCheckBox->setText(QApplication::translate("Dialog", "Windows", nullptr));
        bsdCheckBox->setText(QApplication::translate("Dialog", "BSD", nullptr));
        oracleCheckBox->setText(QApplication::translate("Dialog", "Oracle", nullptr));
        macosCheckBox->setText(QApplication::translate("Dialog", "macOS", nullptr));
        centosCheckBox->setText(QApplication::translate("Dialog", "Centos", nullptr));
        debianCheckBox->setText(QApplication::translate("Dialog", "Debian", nullptr));
        fedoraCheckBox->setText(QApplication::translate("Dialog", "Fedora", nullptr));
        downloadReposButton->setText(QApplication::translate("Dialog", "Download Repos", nullptr));
        label->setText(QApplication::translate("Dialog", "Configure Repos", nullptr));
        ubuntuCheckBox->setText(QApplication::translate("Dialog", "Ubuntu", nullptr));
        prepareIsoButton->setText(QApplication::translate("Dialog", "prepare_iso", nullptr));
#ifndef QT_NO_TOOLTIP
        gitResetHardButton->setToolTip(QApplication::translate("Dialog", "Revert all the changes back to the last git checkin", nullptr));
#endif // QT_NO_TOOLTIP
        gitResetHardButton->setText(QApplication::translate("Dialog", "git reset --hard", nullptr));
#ifndef QT_NO_TOOLTIP
        gitPullButton->setToolTip(QApplication::translate("Dialog", "Get the newest files from the boxcutter repos", nullptr));
#endif // QT_NO_TOOLTIP
        gitPullButton->setText(QApplication::translate("Dialog", "git pull", nullptr));
        label_2->setText(QApplication::translate("Dialog", "Repos Path", nullptr));
        proxyButton->setText(QApplication::translate("Dialog", "proxy setup", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // CONFIGUREREPOS_H
